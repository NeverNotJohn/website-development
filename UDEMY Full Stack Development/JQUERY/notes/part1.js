// Same as .querySelectAll
let heading = $('h1');

//use .css for any css
heading.css( 'color', 'red')

// can use objects:
const theme = {
    'color': 'white',
    'background': 'red',
    'border': '20px solid blue'

}

heading.css(theme)

// can choose from list of identifiers
const listItems = $('li')
listItems.css('color', 'orange')

// can even do negative
listItems.eq(-1).css('color', 'blue')

$('h1').text("WOW I CAN CHANGE TEXT LIKE THIS")

// can change the actual html
$('h1').html('<em>new</em>')

// giving funcionality to the input stuff
$('input').eq(1).attr('type', 'checkbox')
$('input').eq(0).val('new value!')

// adding clases
$('p').addClass('turnRed')

$('input').toggleClass('turnBlue')