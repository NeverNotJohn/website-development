const tick = document.getElementsByClassName("work")
const button = document.querySelector("button")

function changeMarker(me) {
    if (me.textContent == "O" && me.style.color == "white") {
        me.textContent = "X"
        me.style.color = "black"
    }
    else if (me.textContent == "X") {
        me.textContent = "O"
    }
    else {
        me.style.color = "white"
    }

}

for(let i = 0; i < tick.length; i++) {
    tick[i].addEventListener("click", () =>{
        changeMarker(tick[i])
    })
    tick[i].style.cursor = "pointer"
}

button.style.cursor = "pointer"

button.addEventListener("click", () => {
    for(let i=0; i<tick.length;i++) {
        tick[i].textContent = "O"
        tick[i].style.color = "white"
    }
})