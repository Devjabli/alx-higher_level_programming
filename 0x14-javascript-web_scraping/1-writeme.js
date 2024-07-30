#!/usr/bin/node

// Importing fs module for file system operations
const fs = require('fs');

// Getting the filename from the command line args 2
const filename = process.argv[2];

// Getting the filename from the command line args 3
const content = process.argv[3];

// Use fs.readfile to writefile
fs.writeFile(filename, content, 'utf-8', (error) => {
    // show error if not file exists
    error && console.log(error);
});