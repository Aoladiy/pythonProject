// let user = {
//     name: "Джон",
//     age: 30
// };
// user.sayHi = function () {
//     alert("Привет!");
// };
// user.sayHi();

Product_1 = {
    name: "Harney & Sons Earl Grey Imperial Tea Tin",
    img: "https://m.media-amazon.com/images/I/6105mV97UaL._SX679_.jpg",
    description: "Harney & Sons Earl Grey Imperial Tea Tin - Fine Black Tea with Natural Bergamot - 2.35 Ounces, 30 Sachets",
    href: "products/Harney%20&%20Sons%20Earl%20Grey%20Imperial%20Tea%20Tin.html",
}
if (Product_1.name === document.getElementById("original_name").innerText) {
    document.getElementById("name").innerText = Product_1.name;
} else {
    document.getElementById("name").innerText = "Something went wrong (Product_1.name !== document.getElementById(\"original_name\").innerText)";
}
document.getElementById("img").src = Product_1.img;
document.getElementById("description").innerText = Product_1.description;
document.getElementById("href").href = Product_1.href;


function User(name) {
    this.name = name;
    this.isAdmin = false;
}

let user = new User("Me");
let user1 = new User("My neighbour");
let user2 = new User("Someone else");
document.getElementById("1").innerText = user.name;
document.getElementById("2").innerText = user1.name;
document.getElementById("3").innerText = user2.name;

function Product(name, img, description, href) {
    this.name = name;
    this.img = img;
    this.description = description;
    this.href = href;
}

let Twinings_English_Breakfast_Black_Tea = new Product(
    "Twinings English Breakfast Black Tea",
    "https://m.media-amazon.com/images/I/91ijtoPXZZL._SX425_.jpg",
    "Twinings of London English Breakfast Black Tea Bags, 100 Count (Pack of 1).",
    "products/Twinings%20English%20Breakfast%20Black%20Tea.html"
);

if (Twinings_English_Breakfast_Black_Tea.name === document.getElementById("original_name_1").innerText) {
    document.getElementById("name1").innerText = Twinings_English_Breakfast_Black_Tea.name;
} else {
    document.getElementById("name1").innerText = "Something went wrong (Twinings_English_Breakfast_Black_Tea.name !== document.getElementById(\"original_name_1\").innerText)";
}
document.getElementById("img1").src = Twinings_English_Breakfast_Black_Tea.img;
document.getElementById("description1").innerText = Twinings_English_Breakfast_Black_Tea.description;
document.getElementById("href1").href = Twinings_English_Breakfast_Black_Tea.href;
