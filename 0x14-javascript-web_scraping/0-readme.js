#!/usr/bin/node
/*
This script will read and print the content of a file.
*/
const read = require('fs');
read.readFile(process.argv[2], 'utf8', (theerror, thedata) => {
  if (theerror) {
    console.error(theerror);
    return;
  }
  console.log(thedata);
});
