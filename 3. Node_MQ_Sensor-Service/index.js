const express = require("express");
const awsIot = require('aws-iot-device-sdk');
let response;
const device = awsIot.device({
    keyPath: "/home/devagya/Downloads/19cf292c88fe52bc4fe760137ac965fb176afae66737fe77dab2d7353df276ae-private.pem.txt",
    certPath: "/home/devagya/Downloads/19cf292c88fe52bc4fe760137ac965fb176afae66737fe77dab2d7353df276ae-certificate.pem.txt",
    caPath: "/home/devagya/Downloads/0.txt",
    clientId: "DHT-Service",
    host: "at5bqbmqwo924-ats.iot.ap-south-1.amazonaws.com",
    reconnectPeriod: 1000,
    keepalive: 60
});

device.on('connect', () => {
    console.log('Connected to AWS IoT');
    device.subscribe('esp32/smoke/pub');
});

device.on('message', (topic, message) => {
    console.log(`Topic: ${topic}`);
    console.log(`Message: ${message.toString()}`);
    response = message.toString();
});

device.on('error', (err) => {
    console.error('AWS IoT Error:', err);
});

const app = express();
const port = 8000;

app.get('/', (req, res) => {
    res.json(response)
});
app.listen(port, () => {
    console.log(`Server is running on port ${port}`);
});