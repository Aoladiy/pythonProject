let second_name = "ochirov";

function revert_string(str) {
    first_step = str.split("");
    second_step = first_step.reverse();
    third_step = second_step.join("");
    return third_step;
}
if (second_name === revert_string(second_name)) {
    document.getElementById("answer5").innerText = second_name + " is palindrome, " + second_name + " = " + revert_string(second_name)
} else {
    document.getElementById("answer5").innerText = second_name + " isn't palindrome, " + second_name + " != " + revert_string(second_name)
}