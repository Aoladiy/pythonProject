// function showMessage() {
//     let message = "Привет, я JavaScript!"; // локальная переменная
//
//     alert(message);
// }
//
// showMessage(); // Привет, я JavaScript!
//
// alert(message); //
//
let is_it_palindrome = prompt("Is it palindrome? ");

function revert_string(str) {
    result = str.split("").reverse().join("");
    if (str === result) {
        document.getElementById("palindrome").innerText = str + " is palindrome, " + str + " = " + result
    } else {
        document.getElementById("palindrome").innerText = str + " isn't palindrome, " + str + " != " + result
    }
}
revert_string(is_it_palindrome)

let arr = [];
for (let i = 0; i < 15; i++) {
    arr.push(Math.floor(Math.random() * 41 - 10));
}
document.getElementById("start_arr").innerText += arr;


function negatives_to_squares(arr) {
    for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
        arr[i] = arr[i] ** 2;
    }
}
    return arr;
}
document.getElementById("negatives_to_squares").innerText = negatives_to_squares(arr);

class Username {
    name;
    constructor(name) {
        this.name = name;
    }
    get name() {
        return this.name;
    }

    show() {
        alert("Привет, " + this.name)
    }
}

let username = new Username(prompt("enter username: "));
document.getElementById("username").innerText = username.name;
username.show();

class Revert {
    name;
    constructor(name) {
        this.name = name;
    }

    revert() {
        this.name = this.name.split("").reverse().join("")
        return this.name;
    }
    get name() {
        return this.name;
    }
}

let revert_my_name = new Revert(prompt("Enter name to revert: "));
document.getElementById("original_name").innerText = revert_my_name.name;
document.getElementById("reverted").innerText = revert_my_name.revert();