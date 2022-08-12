// clicks:
$('h1').click(function() {
    $(this).text("yes")
})

// works on multiple objects!
$('li').click(function() {
    $(this).text("boop")
    alert('ima list ;D')
})

// KEY PRESSING OWO...
// using event.which to grab specific keys
$('input').eq(0).keypress(function(event) {
    if (event.which === 13) {
        $('h3').toggleClass('turnBlue')
    }
})

// on() = eventListener'
$('h1').on('dblclick', function(){
    $(this).toggleClass('turnBlue')
})

$('h1').on('mouseenter', function() {
    $(this).toggleClass('turnBlue')
})

// effects and animations WOAH
$('input').eq(1).on('click', function() {
    $('.container').slideUp(3000)
    $('.container'). fadeOut(3000)
})
