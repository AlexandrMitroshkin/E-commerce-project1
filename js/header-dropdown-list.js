let header = document.getElementById("header");
let selectedOptionArrow = document.querySelector(".selected-option-arrow");
const selectedOption = document.getElementById('selected-option');
const optionsContainer = document.querySelector('.options');
const optionsList = document.querySelectorAll('.option');

function toggleOptions() {
    if (optionsContainer.classList.contains('visible')) {
        optionsContainer.classList.remove('visible');
        header.style.marginBottom = "24px";
        selectedOptionArrow.classList.add("notInverted");
    } else {
        optionsContainer.classList.add('visible');
        header.style.marginBottom = "100px";
        selectedOptionArrow.classList.remove("notInverted");
    }
}

selectedOption.addEventListener('click', toggleOptions);

