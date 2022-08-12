const headOne = document.querySelector("#one")
const headTwo = document.querySelector("#two")
const headThree = document.querySelector("#three")

headOne.addEventListener('mouseover', () => {
    headOne.textContent = "Mouse Currently Over";
    headOne.style.color = "red"
})

headOne.addEventListener('mouseout', () => {
    headOne.textContent = "Hover Over Me!"
    headOne.style.color = 'black'
})

headTwo.addEventListener("click", () => {
    headTwo.textContent = 'uwu <3'
    headTwo.style.color = 'pink'

    setTimeout(() => {
        headTwo.textContent = 'Click Me!'
        headTwo.style.color = 'black'
    }, 1000)
})

headThree.addEventListener('dblclick', () => {
    headThree.textContent = 'oooooo fancy'
    headThree.style.color = 'lavender'
    setTimeout(() => {
        headThree.textContent = 'Double Click Me!'
        headThree.style.color = 'black'
    }, 1000)
})