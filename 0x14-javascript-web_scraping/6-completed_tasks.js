#!/usr/bin/node
/*
This script will compute the number of tasks completed by user id.
*/
const req = require('request');
const completed = {};
req(process.argv[2], { json: true }, (theerror, respo, body) => {
  if (theerror) {
    console.error(theerror);
    return;
  }
  body.forEach((task) => {
    if (task.completed) {
      if (!completed[task.userId]) {
        completed[task.userId] = 1;
      } else {
        completed[task.userId] += 1;
      }
    }
  });
  console.log(completed);
});
