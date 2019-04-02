// functions that create shortcuts:
function qS (selector) {
  return document.querySelector(selector)
}

function qSA (selector) {
  return document.querySelectorAll(selector)
}

function createCard (event) {
  const createCardDiv = qs('#create-card')

  createCardDiv.innerHTML = ''
}
