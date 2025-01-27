let header = document.querySelector(".header");
let selectedOptionArrow = document.querySelector(".selected-option-arrow");
const selectedOption = document.getElementById('selected-option');
const optionsContainer = document.querySelector('.options');
const optionsList = document.querySelectorAll('.option');

selectedOption.addEventListener('click', () => {
    if (optionsContainer.style.display === 'none' || optionsContainer.style.display === '') {
        optionsContainer.style.display = 'block'; 
        header.style.marginBottom = "125px";
        selectedOptionArrow.classList.remove("notInverted");
    } else {
        optionsContainer.style.display = 'none';
        header.style.marginBottom = "0px";
        selectedOptionArrow.classList.add("notInverted");
    }
});

optionsList.forEach(option => {
    option.addEventListener('click', (event) => {
        const link = event.target.getAttribute('data-link');
        optionsList.forEach(opt => opt.classList.remove('selected'));
        event.target.classList.add('selected');
        window.location.href = link;
    });
});

