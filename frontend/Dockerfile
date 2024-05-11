FROM node:20-bullseye-slim

WORKDIR /app

RUN apt-get update

COPY package*.json ./
RUN npm install

COPY . .

CMD [ "npm", "start" ]