var express = require('express');
var server = express();
server.use(express.static(__dirname));

var port = 8000;
server.listen(port);
console.log('Listening on port ' + port);

exports = module.exports = server;