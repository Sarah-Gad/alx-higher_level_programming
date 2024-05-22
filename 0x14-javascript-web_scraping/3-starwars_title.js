#!/usr/bin/node
/*
This script will print the title of a Star Wars movie
where the episode number matches a given integer.
*/
const getreq = require('request');
const editurl = 'https://swapi-api.alx-tools.com/api/films/' + process.argv[2];
getreq(editurl, { json: true }, (theerror, respo, body) => {
  if (theerror) {
    console.log(theerror);
    return;
  }
  console.log(body.title);
});
