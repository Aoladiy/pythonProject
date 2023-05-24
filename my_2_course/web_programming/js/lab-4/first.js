let user = {
    name: "Джон",
    age: 30
};
user.sayHi = function () {
    alert("Привет!");
};
// user.sayHi();

let user_information = {
    name: "Джон",
    age: 30,
    mail: "mail@gmail.com",
    phone: "79999999999",
    address: "Somewhere in Moscow"
};
// alert(user_information.name);
// alert(user_information.age);
// alert(user_information.mail);
document.getElementById("name").innerText = user_information.name;
document.getElementById("age").innerText = user_information.age;
document.getElementById("mail").innerText = user_information.mail;

