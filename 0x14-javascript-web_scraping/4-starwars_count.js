#!/usr/bin/node
/*
this script will prints the number of movies
where the character “Wedge Antilles” is present.
*/
const req = require('request');
let total = 0;
req(process.argv[2], { json: true }, (theerror, respo, body) => {
  if (theerror) {
    console.error(theerror);
    return;
  }
  body.results.forEach((f) => {
    f.characters.forEach((c) => {
      if (c.includes(18)) {
        total += 1;
      }
    });
  });
  console.log(total);
});
