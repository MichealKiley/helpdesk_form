const computer_area = document.querySelector(".computer_button");
const printer_area = document.querySelector(".printer_button");
const other_area = document.querySelector(".other_button");
const computer_button = document.querySelector("#computer_button");
const printer_button = document.querySelector("#printer_button");
const other_button = document.querySelector("#other_button");

computer_area.addEventListener("click", e => {
    computer_button.click()
});

printer_area.addEventListener("click", e => {
    printer_button.click()
});

other_area.addEventListener("click", e => {
    other_button.click()
});