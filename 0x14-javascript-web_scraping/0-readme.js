#!/usr/bin/node

// importing fs module for file system operations
const fs = require('fs');

// Getting the filename from the command line args
let filename = process.argv[2];

// Use fs.readfile toread file asynchronously
fs.readFile(filename, 'utf-8', (err, content) => {
    err ? console.log(err) : console.log(content);;
})