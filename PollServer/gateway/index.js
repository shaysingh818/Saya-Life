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

function pushNotice(res, msg) {
  if (res.finished) {
    console.log('pushNotice - gateway offline');
    return false;
  }
  try {
    res.write(msg);
  } catch (e) {
	  console.log('pushNotice - exception : ' + e);
	  return false;
  }
  return true;
}

var gateways = {};
var addrs = {};

var pub = nano.socket('pub');
pub.bind(nano_addr);

app.post('/gw/*', function (req, res) {
  var path = url.parse(req.url).pathname;
  console.log("path= " + path);
  var gw = path.substr(4).trim();
  if (gw.length == 0) {
    console.log('missing gateway id');
    res.statusCode = 400; //bad request
    res.end('no gw id');
    return;
  }

  var json = '';
  req.on('data', function (data) {
    json += data;
  });

  req.on('end', function() {
    console.log('json = ' + json);
    try {
      let info = JSON.parse(json);
      info.gw = gw;
      info.online = true;
      let notify_msg = JSON.stringify(info); //'{"gw":"' + gw + '", "online":true, "fw_version":" +  }';
	    console.log('pub - ' + notify_msg);
      pub.send(notify_msg);
    } catch (e) {
      console.log('post: json parsing error!');
      res.end('json format error');
      return;
    }
  });
  res.setTimeout(0);
  gateways[gw] = res; //save the response context for server push
  addrs[req.socket.remoteAddress] = gw;

  req.on("close", function() {
    // request closed unexpectedly
    console.log("gw connection close gw - " + gw + " socket - " + req.socket.remoteAddress);
    var addr = addrs[req.socket.remoteAddress];
    gateways[addr] = null;
    let notify_msg = '{"gw":"' + addr + '", "online":false}';
    console.log('pub - ' + notify_msg);
    pub.send(notify_msg);
    var gw_res = gateways[gw];
  });

});

app.put('/gw/*', function (req, res) {
  var path = url.parse(req.url).pathname;
  var gw = path.substr(4).trim();
  if (gw.length == 0) {
    console.log('put: missing gateway id');
    res.statusCode = 400; //bad request
    res.end('no gw id');
    return;
  }

//  var db = new nedb({filename: './db-data'+path+'/meter_report', autoload: true});
  var json = '';
  req.on('data', function (data) {
    json += data;
  });
  var reports;
  req.on('end', function() {
    console.log('meter report string = ' + json);
	if (gateways[gw] == null) { //received message from gateway reported offline
      gateways[gw] = res;
      addrs[req.socket.remoteAddress] = gw;
	  let notify_msg = '{"gw":"' + gw + '", "online":true}';
	  console.log('online message sent: pub - ' + notify_msg);
      pub.send(notify_msg);
    }

    if (json === '') {
      res.end('empty report');
      return;
    }
    let sensor = false;
    try {
      var reports = JSON.parse(json, (key, value) => {
        if (key == "sensor") sensor = true;
        return value;
      });
    } catch (e) {
      console.log('json parsing error!');
      res.end('json format error');
      return;
    }

    reports.gw = gw;
    if (sensor) {
      let notify_msg = JSON.stringify(reports);
      console.log('pub - ' + notify_msg);
      pub.send(notify_msg);
      return;
    }

    var created = moment();

    reports.CreatedDate = created.format("YYYY-MM-DD HH:mm:ss");

    let notify_msg = JSON.stringify(reports);
    console.log('pub - ' + notify_msg);
    pub.send(notify_msg);
    res.end();
  });
})

app.patch('/', function (req, res) {
  console.log('got patch - ');
});

var options = {
  key: fs.readFileSync('./server.key'),
  cert: fs.readFileSync('./server.crt')
}

http2
  .createServer(options, app)
  .setTimeout(0)
  .listen(44304, ()=>{
    console.log(`Server is listening on https://localhost:44304`)
  }
).on('connection', function(socket) {
  console.log("New connection - from " + socket.remoteAddress +':'+ socket.remotePort);
  socket.setKeepAlive(true, 10000); //10 seconds
  socket.on('error', onError.bind({}, socket));

  function onError(socket) {
    console.log('Socket error!', socket);
    console.log('name', socket.name);
  }

  socket.name = socket.remoteAddress + ":" + socket.remotePort;
})

app_ctrl.post('/gw/*', function (req, res) {
//this gets the path ex. www.google.com/help/users returns /help/users
  var path = url.parse(req.url).pathname;
  console.log("path= " + path);
  
  var gw = path.substr(4).trim();
  if (gw.length == 0) {
    console.log('ctrl - missing gateway id');
    res.statusCode = 400; //bad request
    res.end('{"success":false, "error":"No gateway ID"}');
    return;
  }

  var json = '';
  req.on('data', function (data) {
    json += data;
  });

  let seq = '';
  let get = '';
  req.on('end', function() {
    try {
      JSON.parse(json, (key, value) => {
        if (key == "seq") seq = '"seq":'+value+',';
        else if (key == "get") get = value;
        return value;
      });
    } catch (e) {
      console.log(e);
      get = '';
      res.statusCode = 400;
      res.end('{"success":false, "error":"Invalid Request"}');
      return;
    }
    var gw_res = gateways[gw];
    if (!gw_res) {
      console.log('gw not found');
      if (get === 'status') { //currently only to get status
        res.statusCode = 200;
        res.end('{' + seq + '"success":true, "error":"", "online":false}');
        return;
      }
      res.statusCode = 404; //not found
      res.end('{' + seq + '"success":false, "error":"Gateway not online"}');
    }
    else {
      if (get === 'status') { //currently only to get status
        res.statusCode = 200;
        res.end('{' + seq + '"success":true, "error":"", "online":true}');
        return;
      }
      console.log('sending - ' + json + ' to ' + gw);
      if (pushNotice(gw_res, json)) {
        res.statusCode = 200;
        res.end('{' + seq + '"success":true, "error":""}');
      }
      else {
        res.statusCode = 404;
        res.end('{' + seq + '"success":false, "error":"Meter not online"}');
      }
    }
//    res.end();
  });
})

http
  .createServer(app_ctrl)
  .listen(8080, ()=>{
    console.log(`Ctrl is listening on https://localhost:8080`)
  }
).on('connection', function(socket) {
  console.log("New ctrl connection - from " + socket.remoteAddress +':'+ socket.remotePort);
})
