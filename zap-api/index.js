const { Client, LocalAuth, MessageMedia } = require('whatsapp-web.js');
const qrcode = require('qrcode-terminal');
const express = require('express');
const multer = require('multer');

const app = express();

app.use(express.json());
app.use(express.urlencoded({ extended: true }));

const upload = multer({ 
    storage: multer.memoryStorage(),
    limits: { fileSize: 15 * 1024 * 1024 }
});
const isDocker = process.env.IS_DOCKER === 'true';

const client = new Client({
    authStrategy: new LocalAuth(),
    puppeteer: { 
        executablePath: isDocker ? '/usr/bin/chromium' : undefined,
        args: [
            '--no-sandbox', 
            '--disable-setuid-sandbox',
            '--disable-dev-shm-usage',
            '--disable-extensions',
            '--no-zygote',       // Adicione este
            '--single-process'
        ] 
    }
});


client.on('qr', (qr) => qrcode.generate(qr, { small: true }));
client.on('ready', () => console.log('🚀 WhatsApp conectado e pronto!'));
client.on('auth_failure', (msg) => console.error('❌ Falha na autenticação:', msg));

client.initialize();

app.post('/send', upload.single('imagem'), async (req, res) => {
    const { destino, mensagem } = req.body;
    const arquivo = req.file;

    if (!destino) {
        return res.status(400).json({ erro: "O campo 'destino' é obrigatório." });
    }

    try {
        const jid = (destino.includes('@')) 
            ? destino 
            : `${destino.replace(/\D/g, '')}@c.us`;

        if (arquivo) {
            const media = new MessageMedia(
                arquivo.mimetype,
                arquivo.buffer.toString('base64'),
                arquivo.originalname || 'arquivo'
            );
            
            await client.sendMessage(jid, media, { caption: mensagem || '' });
        } else {
            await client.sendMessage(jid, mensagem || '');
        }

        res.json({ status: "Sucesso", enviadoPara: jid });
    } catch (error) {
        console.error("Erro no envio:", error);
        res.status(500).json({ erro: "Falha ao enviar mensagem", detalhes: error.message });
    }
});

app.get('/list', async (req, res) => {
    try {
        const chats = await client.getChats();
        const grupos = chats
            .filter(chat => chat.isGroup)
            .map(g => ({
                nome: g.name,
                id: g.id._serialized
            }));
        res.json(grupos);
    } catch (error) {
        res.status(500).json({ erro: "Erro ao listar grupos." });
    }
});

// Rota: GET http://localhost:3000/group/123456789@g.us
app.get('/group/:id', async (req, res) => {
    const groupId = req.params.id;

    try {
        // Busca o chat pelo ID fornecido na URL
        const chat = await client.getChatById(groupId);

        if (!chat.isGroup) {
            return res.status(404).json({ erro: "Este ID não pertence a um grupo." });
        }

        // Extrai apenas as informações dos contatos (membros)
        const membros = chat.participants.map(p => ({
            id: p.id._serialized,
            admin: p.isAdmin || p.isSuperAdmin,
        }));

        res.json({
            nome: chat.name,
            id: chat.id._serialized,
            totalMembros: membros.length,
            membros: membros
        });

    } catch (error) {
        console.error("Erro ao buscar grupo:", error);
        res.status(500).json({ 
            erro: "Grupo não encontrado ou erro na busca.", 
            detalhes: error.message 
        });
    }
});

app.listen(3000, () => console.log('🌐 Microsserviço rodando na porta 3000'));