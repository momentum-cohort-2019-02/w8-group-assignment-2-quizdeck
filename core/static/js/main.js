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

// Takes an array and returns the same array but in a random order
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

function get_cards(url) {
  // Gets Json data with all cards listed as question/answer couples
  return (fetch(url)
    .then(function(response) {
      if (!response.ok) {
        throw Error(response.statusText)
      }
      return response.json()
    })

    // Then shuffle the list of cards randomly
    .then(function(data) {
      let cards = shuffle(data['cards'])
      console.log(cards)
      return cards
    }))
}

function addMarkButtons(div, card_div, answeredCards) {
  // Listener to mark right or wrong
  div.addEventListener('click', function(event) {
    let bool = event.target.classList[0]
    let body = {'mark': bool, 'card_question': card_div.innerHTML}
    fetch('/core/mark_card/', {method: 'POST', headers: {'X-CSRFToken': Cookies.get('csrftoken'),'Content-Type': 'application/json'}, body: JSON.stringify(body)})
      .then(response => response.json()).then(function(data) {
        answeredCards.push(card_div.innerHTML)
        console.log(data)
        div.innerHTML = data['ok']
      })
  })
}

function play(cards) {
  // Shows the question of the first card in the shuffled list
  let card_div = document.querySelector('.card')
  let card = cards[0]
  let answeredCards = []
  card_div.innerHTML = card[0]

  // Listener to flip the card
  card_div.addEventListener('click', function () {
    if (card.indexOf(card_div.innerHTML) === 0) {
      card_div.innerHTML = card[1]
    } else { card_div.innerHTML = card[0] }
  })

  // Listener to switch between cards
  qS('.quiz-nav-buttons').addEventListener('click', function(event) {
    if ((event.target.innerHTML === 'Previous') && cards.indexOf(card) > 0) {
      card = cards[cards.indexOf(card)-1]
    } else if ((event.target.innerHTML === 'Next') && cards.indexOf(card) < cards.length-1) {
      card = cards[cards.indexOf(card)+1]
    }
    card_div.innerHTML = card[0]
    if (!(answeredCards.includes(card_div.innerHTML))){
      qS('.right-wrong-buttons').innerHTML = '<div class="right">I got it right!</div><div class="wrong">Show me again...</div>'
    } else {qS('.right-wrong-buttons').innerHTML = '<span>You already answered.</span>'}
  })
  
  addMarkButtons(qS('.right-wrong-buttons'), card_div, answeredCards)
}


// Checking to make sure we are on the right page
if ( document.URL.includes("random_play") ) {
  window.addEventListener('DOMContentLoaded', function () {
    get_cards('/core/get_cards/').then(cards => play(cards))
  })
}

if ( document.URL.includes("play_deck") ) {
  let urlWords = document.URL.split('/')
  let deckSlug = urlWords[urlWords.length-2]
  window.addEventListener('DOMContentLoaded', function () {
    get_cards(`/core/get_deck/${deckSlug}`).then(cards => play(cards))
  })
}

