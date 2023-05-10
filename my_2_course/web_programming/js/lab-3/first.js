let arr = [];
for (let i = 0; i < 15; i++) {
    arr.push(Math.floor(Math.random() * 41 - 10));
}
// 1
let positive_sum = 0;
let positive_count = 0;
let negative_sum = 0;
let negative_count = 0;
let number_of_zeroes = 0;
for (let i = 0; i < arr.length; i++) {
    if (arr[i] > 0) {
        positive_sum += arr[i];
        positive_count++;
    }
    if (arr[i] < 0) {
        negative_sum += arr[i];
        negative_count++;
    }
    if (arr[i] === 0) {
        number_of_zeroes += 1;
    }
}
let positive_average = positive_sum / positive_count;
let negative_average = negative_sum / negative_count;
document.getElementById("1_massive").innerText = "Начальный массив: " + arr;
document.getElementById("1").innerText = "Среднее арифметическое положительных элементов: " + positive_average;
document.getElementById("3_negative").innerText = "Среднее арифметическое отрицательных элементов: " + negative_average;
document.getElementById("3_zeroes").innerText = "Кол-во нулей: " + number_of_zeroes;

// 2
for (let i = 0; i < arr.length; i++) {
    if (arr[i] < 0) {
        arr[i] = arr[i] ** 2;
    }
}
document.getElementById("2_massive").innerText = arr;

// 3
let red_count = 0;
let max_red_count = 0;


for (let i = 0; i < 1000000; i++) {
    let random_num = Math.floor(Math.random() * 3);
    if (random_num === 0) {
        red_count++;
        if (red_count > max_red_count) {
            max_red_count = red_count;
        }
    } else {
        red_count = 0;
    }
}

document.getElementById("4").innerText = "Fourth task: " + max_red_count;