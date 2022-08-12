
const token = $('.token')
let turn = 0

let y1Num = 0
let y2Num = 0
let y3Num = 0
let y4Num = 0
let y5Num = 0
let y6Num = 0
let y7Num = 0

playerOne = prompt("Player One waz ur name ;D: ")
playerTwo = prompt("Player Two wz UR name :D;")

$("#name").text(playerOne + "'s turn:")

function play(ele) {
    if (0 === turn % 2) {
        $(ele).css("background-color", "red")
        $("#name").text(playerTwo + "'s turn:")
    }
    if (1 === turn % 2) {
        $(ele).css("background-color", "blue")
        $("#name").text(playerOne + "'s turn:")
    }
    turn++
}

token.click(function() {
    let x = getClassVal(this, 1)
    
    row = ($(this).closest('tr'))[0]
    yy = getClassVal(row, 0)
    console.log(x)

    if (x == "x1") {
      y1Num++
      y = y1Num
    }
    if (x == "x2") {
      y2Num++
      y = y2Num
    }
    if (x == "x3") {
      y3Num++
      y = y3Num
    }
    if (x == "x4") {
      y4Num++
      y = y4Num
    }
    if (x == "x5") {
      y5Num++
      y = y5Num
    }
    if (x == "x6") {
      y6Num++
      y = y6Num
    }
    if (x == "x7") {
      y7Num++
      y = y7Num
    }
    
    xCoord = '.' + x
    yCoord = '.y' + y

    console.log(yCoord)

    test = $(yCoord).find(xCoord)[0]
    play(test)
})

function getClassVal(element, classNameOrIndex) {
    var listClass = element.classList;
    var classValue = '';
    
    switch(typeof classNameOrIndex) {
      case 'string':
        for(var i = 0; i < listClass.length; i++) {
          if (listClass[i] === classNameOrIndex) {
            classValue = listClass[i];
          }
        }
        break;
        
      case 'number':
        classValue = listClass[classNameOrIndex];
        break;
        
      default:
        classValue = listClass.value;
        break;
    }
    return classValue
}
