#!/usr/bin/node
/*
This script will write a string to a file.
*/
const writer = require('fs');
writer.writeFile(process.argv[2], process.argv[3], 'utf8', (theerror) => {
  if (theerror) {
    console.error(theerror);
  }
});
