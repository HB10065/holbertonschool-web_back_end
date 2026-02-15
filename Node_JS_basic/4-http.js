const http = require('http');

const server = http.createServer((request, response) => {
    response.statusCode = 200;
    response.setHeader('Content-Type', 'text/plain');
    response.end('Hello Holberton School!');
});

server.listen(1245);

module.exports = server;
