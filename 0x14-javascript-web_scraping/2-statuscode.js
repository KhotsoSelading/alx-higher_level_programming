#!/usr/bin/node

/**
 * A script that displays the status code of a GET request using axios.
 */
const axios = require('axios');

const url = process.argv[2];

if (url) {
  axios.get(url)
    .then(response => {
      console.log(`code: ${response.status}`);
    })
    .catch(error => {
      if (error.response) {
        console.log(`code: ${error.response.status}`);
      } else {
        console.error('Error:', error.message);
      }
    });
} else {
  console.error('Usage: node script.js <URL>');
}
