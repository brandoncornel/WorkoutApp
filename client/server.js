var express = require('express');
var server = express();
server.use(express.static(__dirname));

var port = process.env.PORT || 8081;
server.listen(port);
console.log('Listening on port' + port);

exports = module.exports = server;