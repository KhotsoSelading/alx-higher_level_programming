#!/usr/bin/node
/**
 * A script that writes a string to a file.
 */
const fs = require('fs').promises;

async function writeToFile(filePath, content) {
  try {
    await fs.writeFile(filePath, content, 'utf-8');
    console.log('File written successfully.');
  } catch (error) {
    console.error(error);
  }
}

const [filePath, content] = process.argv.slice(2);

if (filePath && content) {
  writeToFile(filePath, content);
} else {
  console.error('Usage: node script.js <file-path> <content>');
}
