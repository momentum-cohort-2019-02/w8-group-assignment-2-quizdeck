/* globals fetch */
const Cookies = require('js-cookie')
const deepmerge = require('deepmerge')

function qS (selector) {
  return document.querySelector(selector)
}

function qSA (selector) {
  return document.querySelectorAll(selector)
}

// This function will be helpful if we need to fetch anything from an API, for example, fetching trivia questions from this API: https://opentdb.com/api_config.php
function request (url, options) {
  if (!options) {
    options = {}
  }
  const defaultOptions = {
    headers: { 'X-CSRFToken': Cookies.get('csrftoken'), 'X-Requested-With': 'XMLHttpRequest' }
  }

  return fetch(url, deepmerge(defaultOptions, options))
}

function shuffle(array) {
  var currentIndex = array.length, temporaryValue, randomIndex;

  // While there remain elements to shuffle...
  while (0 !== currentIndex) {

    // Pick a remaining element...
    randomIndex = Math.floor(Math.random() * currentIndex);
    currentIndex -= 1;

    // And swap it with the current element.
    temporaryValue = array[currentIndex];
    array[currentIndex] = array[randomIndex];
    array[randomIndex] = temporaryValue;
  }

  return array;
}

// Checks to make sure the right page is loaded by looking at url
if ( document.URL.includes("random_play") ) {
  window.addEventListener('DOMContentLoaded', function () {

    // Fetches all cards from database from the get_cards view, returned as question / answer pairs
    fetch('/core/get_cards/')
      .then(function(response) {
        if (!response.ok) {
          throw Error(response.statusText)
        }
        return response.json()
      })

      // Shuffles the returned cards into a randomized list of question / answer pairs
      .then(function(data) {
        cards = shuffle(data['cards'])
        return cards
      })

      // Play functionality
      .then(function(cards) {

        // Displays the first card in the random list in the card html holder
        let card_div = document.querySelector('.card')
        let card = cards[0]
        card_div.innerHTML = card[0]

        // Event listener to toggle between question / answer
        card_div.addEventListener('click', function() {
          if (card.indexOf(card_div.innerHTML) === 0) {
            card_div.innerHTML = card[1]
          } else { card_div.innerHTML = card[0] }
        })

        // Event listener to go between cards
        qS('.quiz-nav-buttons').addEventListener('click', function(event) {
          if ((event.target.innerHTML === 'Previous') && cards.indexOf(card) > 0) {
            card = cards[cards.indexOf(card)-1]
          } else if ((event.target.innerHTML === 'Next') && cards.indexOf(card) < cards.length-1) {
            card = cards[cards.indexOf(card)+1]
          }
          card_div.innerHTML = card[0]
        })
      })
        
  })
}
