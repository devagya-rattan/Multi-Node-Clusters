FROM node:22-alpine

WORKDIR app/

COPY package*.json ./

COPY private.pem.txt app/
COPY certificate.pem.txt app/
COPY AmazonRootCA1.txt app/


RUN npm install

COPY . .

EXPOSE 3000

CMD ["node","index.js"]