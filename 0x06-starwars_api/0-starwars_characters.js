#!/usr/bin/node

const httpRequest = require('request');

httpRequest('https://swapi-api.hbtn.io/api/films/' + process.argv[2], function (error, response, responseBody) {
  if (error) throw error;
  const characterUrls = JSON.parse(responseBody).characters;
  processCharacters(characterUrls, 0);
});

const processCharacters = (characterUrls, index) => {
  if (index === characterUrls.length) return;
  httpRequest(characterUrls[index], function (error, response, responseBody) {
    if (error) throw error;
    console.log(JSON.parse(responseBody).name);
    processCharacters(characterUrls, index + 1);
  });
};
