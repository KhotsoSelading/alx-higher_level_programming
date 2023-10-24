#!/usr/bin/node

/**
 * A script that displays the status code of a GET request.
 */
const axios = require('axios');

async function getStatus(url) {
  try {
    const response = await axios.get(url);
    console.log(`code: ${response.status}`);
  } catch (error) {
    if (error.response) {
      console.log(`code: ${error.response.status}`);
    } else {
      console.error('Error:', error.message);
    }
  }
}

const url = process.argv[2];

if (url) {
  getStatus(url);
} else {
  console.error('Usage: node script.js <URL>');
}
