const yes_area = document.querySelector(".yes_button");
const no_area = document.querySelector(".no_button");
const yes_button = document.querySelector("#y_button");
const no_button = document.querySelector("#n_button");

yes_area.addEventListener("click", e => {
    yes_button.click()
});

no_area.addEventListener("click", e => {
    no_button.click()
});

