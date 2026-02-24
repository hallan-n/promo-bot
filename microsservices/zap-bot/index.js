import makeWASocket, {
    useMultiFileAuthState,
    fetchLatestBaileysVersion,
    DisconnectReason
} from '@whiskeysockets/baileys'
import P from 'pino'
import QRCode from 'qrcode-terminal'
import fs from 'fs'
import express from 'express'
import multer from 'multer'
import path from 'path'

const AUTH_PATH = path.resolve('./auth')
let sock = null

async function _getSock() {
    if (sock) return sock

    const { state, saveCreds } = await useMultiFileAuthState(AUTH_PATH)
    const { version } = await fetchLatestBaileysVersion()

    sock = makeWASocket({
        version,
        logger: P({ level: 'info' }),
        auth: state,
        browser: ['Ubuntu', 'Chrome', '120.0.0']
    })

    sock.ev.on('creds.update', saveCreds)

    await new Promise((resolve, reject) => {
        sock.ev.on('connection.update', (update) => {
            const { connection, lastDisconnect, qr } = update

            if (qr) {
                console.log('\n📱 ESCANEIE O QR:\n')
                QRCode.generate(qr, { small: true })
            }

            if (connection === 'open') {
                console.log('✅ CONECTADO!')
                resolve(sock)
            }

            if (connection === 'close') {
                const shouldReconnect =
                    lastDisconnect?.error?.output?.statusCode !== DisconnectReason.loggedOut

                console.log('❌ Conexão fechada. Reconectar?', shouldReconnect)

                if (!shouldReconnect) {
                    // Apaga a pasta auth automaticamente
                    if (fs.existsSync(AUTH_PATH)) {
                        fs.rmSync(AUTH_PATH, { recursive: true, force: true })
                        console.log('🗑️ Pasta auth apagada para novo login')
                    }
                    reject(new Error('Desconectado permanentemente'))
                } else {
                    sock = null // força reconectar
                }
            }
        })
    })

    return sock
}

// getSock só gera novo QR se houver erro de autenticação
export async function getSock() {
    return await _getSock()
}

export async function sendMessage(sock, target, message, image) {
    const jid = target.includes('@g.us') ? target : `${target}@s.whatsapp.net`

    if (image) {
        await sock.sendMessage(jid, {
            image: image,
            caption: message || '',
            contextInfo: { previewType: 'none' }
        })
    } else if (message) {
        await sock.sendMessage(jid, {
            text: message,
            contextInfo: { previewType: 'none' }
        })
    } else {
        throw new Error('Nenhuma mensagem ou imagem fornecida')
    }
}

// --- API ---
const app = express()
const upload = multer()
const socket = getSock()

app.post('/send', upload.single('image'), async (req, res) => {
    const { target, message } = req.body
    const image = req.file?.buffer

    try {
        await sendMessage(await socket, target, message, image)
        res.json({ status: 'ok' })
    } catch (err) {
        console.error(err)
        res.status(500).json({ error: err.message })
    }
})

app.listen(3000, () => console.log('API rodando na porta 3000'))