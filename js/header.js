                                            // закрытие регистрации
let headerRegisterClose = document.querySelector(".header-register-close");
let headerRegister = document.querySelector(".header-register");

headerRegisterClose.onclick = function(){
  headerRegister.style.display = "none";
  header.style.paddingTop = "10px" 
  header.style.height = "48px"
}

//                                               реализация кнопки header-nav-more

let headerNavMore = document.querySelector(".header-nav-more");
let headerNavLinks = document.querySelector(".header-nav-links");

headerNavMore.onclick = function(){
  headerNavLinks.classList.toggle("visible");
  headerNavMore.classList.toggle("inverted");
  if (headerNavLinks.classList.contains("visible")){
    header.style.marginBottom = "60px"
  }
}


                                            // реализация выпадающего списка

let header = document.getElementById("header");
let selectedOptionArrow = document.querySelector(".selected-option-arrow");
const selectedOption = document.getElementById('selected-option');
const optionsContainer = document.querySelector('.options');
const optionsList = document.querySelectorAll('.option');

function toggleOptions() {
  if (optionsContainer.classList.contains('visible')) {
    optionsContainer.classList.remove('visible');
    selectedOptionArrow.classList.add("notInverted");
    if (!headerNavLinks.classList.contains('visible')) {
      header.style.marginBottom = "24px";
    }else if(headerNavLinks.classList.contains('visible')){
      header.style.marginBottom = "148px";
    }
    else{
      header.style.marginBottom = "100px";
    }
  } else {
    optionsContainer.classList.add('visible');
    selectedOptionArrow.classList.remove("notInverted");
  }
}

selectedOption.onclick = toggleOptions;

document.onclick = function(event){
  if (!event.target.closest('.select-wrapper')) {
    optionsContainer.classList.remove('visible');
  if (!headerNavLinks.classList.contains('visible') && !optionsContainer.classList.contains('visible')) {
    header.style.marginBottom = "24px";
  }else if(headerNavLinks.classList.contains('visible')){
    header.style.marginBottom = "60px";
  }else if (headerNavLinks.classList.contains('visible') && optionsContainer.classList.contains('visible')){
    header.style.marginBottom = "148px";
  }
  }
}

                                                        // реализация search

const input = document.getElementById('header-nav-input');
const customDatalist = document.getElementById('custom-datalist');
let headerNavSearch = document.querySelector(".header-nav-search");

const data = {
  "thing1": "https://trychatgpt.ru/",
  "thing2": "https://github.com/",
  "thing3": "#",
  "thing4": "#",
  "thing5": "#",
  "thing6": "#",
  "thing7": "#",
  "thing8": "#",
  "thing9": "#",
  "thing10": "#"
};

  function updateDatalist() {
  const inputValue = input.value.toLowerCase();
  const filteredData = Object.keys(data).filter(item => {
    return item.toLowerCase().includes(inputValue);
  });

  customDatalist.innerHTML = '';

  if (inputValue && filteredData.length > 0) {
    filteredData.forEach(item => {
      const option = document.createElement('a');
      option.textContent = item;
      option.setAttribute('href', data[item]);
      option.onclick = function(){
        input.value = item;
        customDatalist.classList.remove('show');
        if (!optionsContainer.classList.contains('visible') && !headerNavLinks.classList.contains('visible')) {
          header.style.marginBottom = "24px";
        }else{
          header.style.marginBottom = "60px";
        }
      };
      customDatalist.appendChild(option);
    });

    switch (filteredData.length) {
      case 1:
        if(!optionsContainer.classList.contains('visible')){
            header.style.marginBottom = "61.5px";
        }
        else{
            header.style.marginBottom = "100px";
        }
        break;
      case 2:
        header.style.marginBottom = "100px";
        break;
      case 3:
        header.style.marginBottom = "136.5px";
        break;
      default:
        header.style.marginBottom = "174px";
        break;
    }

    customDatalist.classList.add('show');
  } else {
    customDatalist.classList.remove('show');
    if (!optionsContainer.classList.contains('visible') && !headerNavLinks.classList.contains('visible')) {
      header.style.marginBottom = "24px";
    }else if (headerNavLinks.classList.contains('visible')){
      header.style.marginBottom = "60px";
    }
  }
}

input.addEventListener('input', updateDatalist);

document.addEventListener('click', (event) => {
  if (!event.target.closest('.header-nav-search')) {
    customDatalist.classList.remove('show');
    if (!optionsContainer.classList.contains('visible') && !headerNavLinks.classList.contains('visible')) {
      header.style.marginBottom = "24px";
    }else if (!optionsContainer.classList.contains('visible') && headerNavLinks.classList.contains('visible')){
      header.style.marginBottom = "60px";
    }else if (optionsContainer.classList.contains('visible') && headerNavLinks.classList.contains('visible')){
      header.style.marginBottom = "148px";
    }
    else if (optionsContainer.classList.contains('visible') && !headerNavLinks.classList.contains('visible')){
      header.style.marginBottom = "100px";
    }
  }
});
























                                            