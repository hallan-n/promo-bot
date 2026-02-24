# Use Node LTS
FROM node:20-bullseye

# Diretório de trabalho dentro do container
WORKDIR /usr/src/app

# Copia package.json e package-lock.json
COPY package*.json ./

# Instala dependências
RUN npm install

# Copia todo o restante do projeto
COPY . .

# Expõe porta 3000 da API
EXPOSE 3000

# Comando para rodar o bot
CMD ["node", "src/api.js"]