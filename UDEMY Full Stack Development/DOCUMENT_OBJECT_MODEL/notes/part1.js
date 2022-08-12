const myheader = document.querySelector("h1")

function getRandomColor() {
    var letters = '0123456789ABCDEF';
    var color = '#';
    for (var i = 0; i < 6; i++) {
      color += letters[Math.floor(Math.random() * 16)];
    }
    return color;
  }

function changeColor(color) {
    myheader.style.color = color
}
  
// do it over a set of intervalls... millisecnds

setInterval("changeColor(getRandomColor())", 500)
