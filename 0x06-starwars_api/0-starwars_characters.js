#!/usr/bin/node
const request = require('request');

if (process.argv.length !== 3) {
  console.error('Usage: ./0-starwars_characters.js <Movie ID>');
  process.exit(1);
}

const movieId = process.argv[2];
const apiUrl = `https://swapi.dev/api/films/${movieId}/`;

request(apiUrl, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    process.exit(1);
  }

  const movieData = JSON.parse(body);
  const characters = movieData.characters;

  const fetchCharacter = (characterUrl) => {
    request(characterUrl, (charError, charResponse, charBody) => {
      if (charError) {
        console.error('Error:', charError);
        process.exit(1);
      }

      if (charResponse.statusCode !== 200) {
        console.error('Invalid response:', charResponse.statusCode);
        process.exit(1);
      }

      const character = JSON.parse(charBody);
      console.log(character.name);
    });
  };

  for (const characterUrl of characters) {
    fetchCharacter(characterUrl);
  }
});
