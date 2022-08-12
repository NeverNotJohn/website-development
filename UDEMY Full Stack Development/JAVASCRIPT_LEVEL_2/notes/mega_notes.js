// FUNCTIONS!!!

function print(input) {
    // i luv python <3
    console.log(input)
}

// main:

print("hello!")

// Practice:

function sleepIn(weekday, vacation) {
    if(!weekday || vacation) {
        return true
    }
}

console.log(sleepIn(true, true))

// ARRAYS!!!

var stuff = ["wow this is great", 22, "very much ez", 'c', 22.5]
console.log(stuff)
console.log(stuff[0])

// practice on assessments

// OBJECTS... they are hastables... aka dictinaries in python 

// key: object
let user_101 = {name: "John", age: 17, race: "Filipino"}

// calling object based on key:
user_101['John']

// can store like anything

let what = {a: [1, 2, 3, 4], b: 112938102983.5, c:{inside: [ 4 ,5, ["weird"]]}}

// grab 2:
console.log("I grabbed le " + what['a'][1])

// changing based on key:
user_101['name'] = "Juanita"
console.log(user_101['name'])

// show entire object:
console.dir(user_101)

// bro u can do python styled for loops

for (let key in user_101) {
    console.log(key + " " + user_101[key] + "\n")
}

// u can make functions in object called methods!

let user_888 = {
    name: "Robert",
    age: 19,
    race: "dinosaur",
    kill: function(){
        console.log("You have killed " + this.name + ", congrats!")
    }
}

console.dir(user_888)
user_888.kill()