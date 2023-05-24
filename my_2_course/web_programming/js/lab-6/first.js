const add = (a, b) => a + b;
const subtract = (a, b) => a - b;
const multiply = (a, b) => a * b;
const divide = (a, b) => a / b;

const calculator = (a, operation, b) => {
    switch (operation) {
        case "+":
            return add(a, b);
        case "-":
            return subtract(a, b);
        case "*":
            return multiply(a, b);
        case "/":
            return divide(a, b);
        default:
            return "Invalid operation";
    }
};

document.getElementById("calculator").innerText = calculator(prompt("first number: "), prompt("operation: "), prompt("second number: "));

const calculateAverage = arr => {
  const sum = arr.reduce((total, num) => total + num, 0);
  const avg = sum / arr.length;
  return avg;
};

let arr = [];
for (let i = 0; i < 15; i++) {
    arr.push(Math.floor(Math.random() * 41 - 10));
}
document.getElementById("arr").innerText += arr;
document.getElementById("average").innerText = calculateAverage(arr);