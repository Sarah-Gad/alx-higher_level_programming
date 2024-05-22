#!/usr/bin/node
/*
This script will display the status code of a GET request.
*/
const getReq = require('request');
getReq(process.argv[2], (theerror, respo, body) => {
  if (theerror) {
    console.error(theerror);
    return;
  }
  console.log(`code: ${respo.statusCode}`);
});
