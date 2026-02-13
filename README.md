# 🤖 Promo Bot

Promo Bot é uma aplicação desenvolvida em **Python** que automatiza a busca e divulgação de produtos promocionais da Amazon e outras lojas, gerando links de afiliados e enviando ofertas automaticamente para grupos de WhatsApp de achadinhos.

---

## 🚀 Funcionalidades

- 🔎 Busca automática de produtos em lojas online
- 🔗 Geração automática de links de afiliados
- 💰 Identificação de descontos e promoções
- 📤 Envio automático de ofertas para grupos do WhatsApp
- ⚡ Processamento assíncrono e otimizado
- 🧠 Cache e controle de tarefas utilizando Redis

---

## 🛠️ Tecnologias Utilizadas

- **Python**
- **Playwright** → Automação do navegador e scraping
- **Redis** → Gerenciamento de filas, cache e tarefas

---

## 📦 Como Funciona

1. O bot acessa lojas online utilizando automação com Playwright.
2. Os produtos são coletados e analisados.
3. O sistema gera automaticamente o link de afiliado.
4. As promoções são formatadas.
5. O bot envia as ofertas para grupos de WhatsApp.

---

## ⚙️ Requisitos

- Python 3.10+
- Redis instalado e rodando
- Navegadores do Playwright instalados

---

## 📥 Instalação

### Clone o projeto

```bash
git clone https://github.com/hallan-n/promo-bot.git
cd promo-bot
