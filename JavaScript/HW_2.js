var min;
var max; 
var letters; 
var capital_lett;
var number;
var dog;
var notEmpty;

function validScript(name){

    if (typeof name == "string") {

        if (name.length < 5) {
            console.log("Должно быть не менее 5 символов")
        }
        else  {
          min = true
        }

        if (name.length > 64) {
            console.log("Должно быть не более 64 символов")
        }
        else  {
          max = true
        }  

        if (/\w/.test(name))
        {
          letters = true
        }
        else  {
          console.log("Должны быть буквы")
        } 

        if (/[A-Z]/.test(name))
        {
          capital_lett = true
        }
        else  {
          console.log("Должна быть хотя бы одна буква в верхнем регистре")
        } 

        if (/\d/.test(name))
        {
          number = true
        }
        else  {
          console.log("Должна быть хотя бы одна цифра")
        }
        
        if (/\@/.test(name))
        {
          dog = true
        }
        else  {
          console.log("Должна быть @")
        } 

        if (!name) {
            console.log("Строка не должна быть пустой")
        }
        else  {
          notEmpty = true
        }  

        if (min && max && letters && capital_lett && number && dog && notEmpty) {
            console.log("Строка корректная")
        }
    }
    
    else { 
    console.log("Ошибка. Некорректная строка")
    } 
};  

validScript("123A@");
