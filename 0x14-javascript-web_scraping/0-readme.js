#!/usr/bin/node

// Import the 'fs' module for file system operations
const fs = require('fs');

// Get the filename from the command-line arguments
const filename = process.argv[2];

// Use 'fs.readFile' to read the file asynchronously
fs.readFile(filename, 'utf-8', (err, content) => {
  // If an error occurred, log it to the console
  if (err) {
    console.log(err);
  } else {
    // Otherwise, print the content of the file
    console.log(content);
  }
});