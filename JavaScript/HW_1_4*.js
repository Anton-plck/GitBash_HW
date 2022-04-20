// 4***: Преобразовать задание 3* таким образом, чтобы возраст вводится используя функцию prompt в привязанной верстке

let age_2 = 18
let age_3 = 60
checkAge(prompt("Enter your age"))

function checkAge (age) {
    if (isNaN(age)) {
        alert("Error. Age is not number")
        console.log ("Error. Age is not number")
    }
    else {
        if (age < age_2) {
            alert ("You don't have access cause your age is " + age + ".", "It's less then", age_2)
            console.log("You don't have access cause your age is " + age + ".", "It's less then", age_2)
        }
        else if (age >= age_2 && age < age_3){
            alert ("Welcome!")
            console.log("Welcome")
            }
        else if (age > age_3){
            alert ("Keep calm and look Culture channel")
            console.log ("Keep calm and look Culture channel")
            }    
        else {
            alert ("Technical work")
            console.log ("Technical work")
        }
    }
}    
