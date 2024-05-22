#!/usr/bin/node
/*
this script will get the contents of a webpage and stores it in a file.
*/
const req = require('request');
const writer = require('fs');
req(process.argv[2], (theerror, respo, body) => {
  if (theerror) {
    console.error(theerror);
    return;
  }
  writer.writeFile(process.argv[3], body, 'utf8', (error) => {
    if (error) {
      console.error(error);
    }
  });
});
