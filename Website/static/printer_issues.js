const printer_box = document.querySelector("#printer_box")
document.querySelector('.body_field').style.display = "none";


printer_box.addEventListener("change", e =>{
    if(printer_box.value == "Other") {
        document.querySelector('.body_field').style.display = "block";
    }
    if(printer_box.value != "Other") {
        document.querySelector('.body_field').style.display = "none";
    }
})


