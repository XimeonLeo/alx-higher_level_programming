#!/usr/bin/node
// computes the number of tasks completed by user id.

const request = require('request');
const url = process.argv[2];

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
    return;
  }
  const todoList = JSON.parse(body);
  const completed = todoList.filter((dict) => dict.completed);
  console.log(completed);
})
