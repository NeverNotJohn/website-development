let students = []

function stuff(input) {
    if (input == "add") {
        newStudent = prompt("What is this new student's name?")
        students.push(newStudent)
        alert(newStudent + " has been added!")
    }

    if (input == "remove") {
        student = prompt("Who would you like to remove?")
        students.splice(students.indexOf(student), 1)
    }

    if (input == "display") {
        for (let i = 0; i < students.length; i++) {
            console.log(students[i])
        }
    }

    if (input == "quit") {
        alert("ok fine")
    }
}

hi = prompt("Start? y/n")

if (hi == "y") {
    while (true) {
        input = prompt("add, remove, display, or quit?")
        if (input === "quit") {
            break
        }
        stuff(input)
    }
}

else {
    alert("ok fine jeez")
}