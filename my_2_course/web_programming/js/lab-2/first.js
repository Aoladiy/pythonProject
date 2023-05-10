let right_answer = 0;
let answer;
for (let i = 0; i < 3; i++) {
    if (i === 0) {
        answer = prompt("2+2 = ?")
        if (answer == 4) {
            right_answer += 1;
        }
    } else if (i === 1) {
        answer = prompt("2-2 = ?")
        if (answer == 0) {
            right_answer += 1;
        }
    } else if (i === 2) {
        answer = prompt("2+8 = ?")
        if (answer == 10) {
            right_answer += 1;
        }
        document.getElementById("answer").innerText = "кол-во правильных ответов: " + right_answer
    }
}