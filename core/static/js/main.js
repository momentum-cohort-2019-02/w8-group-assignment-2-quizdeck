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

function createCard (input) {
  // finds the div id="create-card" on the create page
  const createCardDiv = qs('#create-card')
  // & sets it to empty
  createCardDiv.innerHTML = ''

  const card = document.createElement('div')



  const question = document.createElement('form')

}

// document.addEventListener('DOMContentLoaded', function () {
  
//   const createCardForm = qs('#create_card')
//   createCardForm.addEventListener('submit', function (event) {
//     event.preventDefault()

//     const cardField = qs('#task-field')
//     const body = {
//       'task': taskField.value
//     }
//     taskField.value = ''

//     request(newTaskForm.action, {
//       method: 'POST',
//       headers: {
//         'Content-Type': 'application/json'
//       },
//       body: JSON.stringify(body)
//     })
//       .then(response => {
//         if (!response.ok) {
//           throw Error(response.statusText)
//         }
//         return response.text()
//       })
//       .then(text => {
//         const taskFragment = htmlToNodes(text)
//         q('#task-list').appendChild(taskFragment)
//       })
//   })
// })