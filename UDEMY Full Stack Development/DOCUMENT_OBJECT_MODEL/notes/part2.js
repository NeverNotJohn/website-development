let paragraph = document.querySelector('p')
paragraph.textContent = "wow this is new :D"
// or directly into html
paragraph.innerHTML = "<strong>I'm bold now :D </strong> "

// grab stuff now

const special = document.querySelector("#special")
// only grab a header
let specialA = special.querySelector("a")
// takes in the attribute you want to change an what you want to change it to
specialA.setAttribute("href", "https://www.amazon.com")