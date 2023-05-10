for (let i = 2; i <= 17; i++) {
    let flag = 1;
    for (let j = 2; (j <= i / 2) && (flag == 1); j = j + 1) {
        if (i % j == 0) {
            flag = 0
        }
    }
    if (flag == 1) {
        document.getElementById("answer").innerText += i + "\n"
    }
}

