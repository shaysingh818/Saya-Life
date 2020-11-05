'use strict';
const http2 = require('spdy')
const logger = require('morgan')
const express = require('express')
const app = express()
const fs = require('fs')
const url = require('url')
const nedb = require('nedb')
const app_ctrl = express()
const http = require('http')
const moment = require('moment')
const uuid = require('uuid')
const nano = require('nanomsg')

const nano_addr = 'tcp://127.0.0.1:8888';

app.use(logger('dev'))

app_ctrl.post('/gw/*', function (req, res) {

    //basically gets the path
    var path = url.parse(req.url).pathname;
    console.log(path); 

    var gw = path.substr(4).trim();
    console.log(gw); 
    if (gw.length == 0) {
        console.log('ctrl - missing gateway id');
        res.statusCode = 400; //bad request
        res.end('{"success":false, "error":"No gateway ID"}');
        return;
    }
    /** 
    var json = '';
    req.on('data', function (data) {
        json += data;
    });
    console.log(json); 
    */

    //this gets BODY DATA

   	var json = '';
  	req.on('data', function (data) {
    	json += data;
  	}); 

  	console.log(json); 

  })


http.createServer(app_ctrl)
  .listen(8080, ()=>{
    console.log(`Ctrl is listening on https://localhost:8080`)
  }
).on('connection', function(socket) {
  console.log("New ctrl connection - from " + socket.remoteAddress +':'+ socket.remotePort);
})
