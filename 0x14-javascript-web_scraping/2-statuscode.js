#!/usr/bin/node

const req = require('request');

const url = process.argv[2];

req.get(url, (error, response) => {
    error ? console.log(error) : console.log(`code: ${response.statusCode}`);
});