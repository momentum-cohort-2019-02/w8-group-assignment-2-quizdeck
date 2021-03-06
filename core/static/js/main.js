/* globals fetch */
const Cookies = require('js-cookie')
const deepmerge = require('deepmerge')
const jquery = require('jquery')
const bootstrap = require('bootstrap')




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

function addMarkButtons(div, card_div, answeredCards, score, cards) {
  // Listener to mark right or wrong
  div.addEventListener('click', function(event) {
    if (event.target.classList[1] === 'answer') {
      let bool = event.target.classList[0]
      let body = {'mark': bool, 'card_question': card_div.innerHTML}
      fetch('/core/mark_card/', {method: 'POST', headers: {'X-CSRFToken': Cookies.get('csrftoken'),'Content-Type': 'application/json'}, body: JSON.stringify(body)})
        .then(response => response.json()).then(function(data) {
          answeredCards.push(card_div.innerHTML)
          score += data['value']
          if (answeredCards.length === cards.length) {
            qS('.play').innerHTML = `<h2 class="end-play">Thanks for playing! You got ${score} out of ${cards.length} correct.</h2>`
          }
          console.log(data)
          div.innerHTML = data['message']
        })
    }
  })
}

function play(cards) {
  // Shows the question of the first card in the shuffled list
  let score = 0
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
    if ((event.target.classList.contains('previous')) && cards.indexOf(card) > 0) {
      card = cards[cards.indexOf(card)-1]
    } else if ((event.target.classList.contains('next')) && cards.indexOf(card) < cards.length-1) {
      card = cards[cards.indexOf(card)+1]
    }
    card_div.innerHTML = card[0]
    if (!(answeredCards.includes(card_div.innerHTML))){
      qS('.right-wrong-buttons').innerHTML = "<div class='right answer'>I got it right!</div><div class='wrong answer'>I don't know</div>"
    } else {qS('.right-wrong-buttons').innerHTML = '<span>You already answered.</span>'}
  })
  
  addMarkButtons(qS('.right-wrong-buttons'), card_div, answeredCards, score, cards)
}


// Checking to see what page we are on before doing stuff
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

if ( document.URL.includes('users') && document.URL.includes('decks') ) {
  qS('.profile-options').addEventListener('click', function(event) {
    let urlWords = document.URL.split('/')
    let username = urlWords[urlWords.length-3]
    let body = {"username": username}
    if (event.target.classList.contains('authored')) {
      body["deckRel"] = 'authored'
    } else if (event.target.classList.contains('owned')) {
      body["deckRel"] = 'owned'
    }
    if (!event.target.classList.contains('active')) {
      qS('.active').classList.remove('active')
      event.target.classList.add('active')
    } 
    fetch('/core/profile_get_decks/', {method: 'POST', body: JSON.stringify(body), headers: {'X-CSRFToken': Cookies.get('csrftoken'),'Content-Type': 'application/json'}})
      .then(function(response) { 
        return response.text()
      })
      .then(text => {
        qS('.profile-decks').innerHTML = text
      })
  })
}

if ( document.URL.includes('users') && document.URL.includes('cards') ) {
  qS('.profile-options').addEventListener('click', function(event) {
    let urlWords = document.URL.split('/')
    let username = urlWords[urlWords.length-3]
    let body = {"username": username}
    if (event.target.classList.contains('authored')) {
      body["cardRel"] = 'authored'
    } else if (event.target.classList.contains('owned')) {
      body["cardRel"] = 'owned'
    }
    if (!event.target.classList.contains('active')) {
      qS('.active').classList.remove('active')
      event.target.classList.add('active')
    } 
    fetch('/core/profile_get_cards/', {method: 'POST', body: JSON.stringify(body), headers: {'X-CSRFToken': Cookies.get('csrftoken'),'Content-Type': 'application/json'}})
      .then(function(response) { 
        return response.text()
      })
      .then(text => {
        qS('.profile-cards').innerHTML = text
      })
  })
}
