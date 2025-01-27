let header = document.querySelector(".header");
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

function selectOption(event) {
    const link = event.target.getAttribute('data-link');
    optionsList.forEach(opt => opt.classList.remove('selected'));
    event.target.classList.add('selected');
    window.location.href = link;
}

selectedOption.addEventListener('click', toggleOptions);
optionsList.forEach(option => {
    option.addEventListener('click', selectOption);
});

