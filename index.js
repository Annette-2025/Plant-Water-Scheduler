var http = require('http');
var fs = require('fs');
var url = require('url');
const port = 1001

http.createServer((req, res)=>{
    var q = url.parse(req.url,true);
    var filename = "."+q.pathname;
    fs.readFile(filename, function(err,data){
        if(err){
            res.writeHead(404,{'Content-Type' : 'text/html'});
            return res.end("Page not found");
        }
        res.writeHead(200, {'Content-Type' : 'text/html'});
        res.write(data);
        return res.end();
    });
    //res.writeHead(200,{'Content-Type': 'text/html'});
    //var readStream = fs.createReadStream('public/plantList.html');
    //readStream.pipe(res);
}).listen(port);
console.log("server running on port " + port + "\nAccess Webpage here: " + "http://localhost:" + port + "/pages/calendar.html");






/*
const express = require('express');
const serverless = require('serverless-http');

const app = express();

app.use(express.json());
app.use(express.urlencoded({extended: true}));
app.use(express.static('public'));

app.get('/main', (req, res) => {
    res.sendFile(__dirname + '/public/index.html');
})

app.post('/main/result', (req, res) => {
    
})
    */