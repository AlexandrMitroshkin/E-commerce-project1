                                            // закрытие регистрации
let headerRegisterClose = document.querySelector(".header-register-close");
let headerRegister = document.querySelector(".header-register");

headerRegisterClose.onclick = function(){
  headerRegister.style.display = "none";
  header.style.paddingTop = "10px" ;
  header.style.height = "48px";
}

                                              // реализация кнопки header-nav-more

let headerNavMore = document.querySelector(".header-nav-more");
let headerNavLinks = document.querySelector(".header-nav-links");

headerNavMore.onclick = function(){
  headerNavSearch.classList.remove("visible");
  headerNavLinks.classList.toggle("visible");
  headerNavMore.classList.toggle("inverted");
  if (headerNavLinks.classList.contains("visible")){
    header.style.marginBottom = "60px";
  }
}

                                            // реализация кнопки Magnifying_glass-button

let MagnifyingGlassButton = document.querySelector(".Magnifying_glass-button");

MagnifyingGlassButton.onclick = function(){
  headerNavSearch.classList.toggle("visible");
  if (headerNavLinks.classList.contains("visible")){
    headerNavLinks.classList.remove("visible");
    headerNavMore.classList.remove("inverted")
  }else if (!headerNavLinks.classList.contains("visible") && 
  !customDatalist.classList.contains('show') && 
  headerNavSearch.classList.contains("visible")){
    header.style.marginBottom = "72px";
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
  }else {
    optionsContainer.classList.add('visible');
    selectedOptionArrow.classList.remove("notInverted");
  }
}

selectedOption.onclick = toggleOptions;

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
        if (!optionsContainer.classList.contains('visible') && 
        !headerNavLinks.classList.contains('visible') && 
        !headerNavSearch.classList.contains("visible")){
          header.style.marginBottom = "24px";
        }else if (headerNavLinks.classList.contains('visible')){
          header.style.marginBottom = "60px";
        }else if(headerNavSearch.classList.contains("visible")){
          header.style.marginBottom = "72px";
        }
      };
      customDatalist.appendChild(option);
    });

    switch (filteredData.length) {
      case 1:
        if(headerNavSearch.classList.contains("visible")){
            header.style.marginBottom = "100px";
        }
        else{
          header.style.marginBottom = "61.5px";
        }
        break;

      case 2: 
        if (headerNavSearch.classList.contains("visible")){
          header.style.marginBottom = "168px";
        }else{
          header.style.marginBottom = "100px";
        }
        break;

      case 3:
        if (headerNavSearch.classList.contains("visible")){
          header.style.marginBottom = "204.5px";
        }else{
          header.style.marginBottom = "136.5px";
        }
        break;

      default:
        if (headerNavSearch.classList.contains("visible")){
          header.style.marginBottom = "242px";
        }else{
          header.style.marginBottom = "174px";
        }
        break;
    }

    customDatalist.classList.add('show');
  } else {
    customDatalist.classList.remove('show');
    if (!optionsContainer.classList.contains('visible') && 
      !headerNavLinks.classList.contains('visible') && 
      !headerNavSearch.classList.contains("visible")){
        header.style.marginBottom = "24px";
    }else if (headerNavLinks.classList.contains('visible')){
      header.style.marginBottom = "60px";
    }else if(headerNavSearch.classList.contains("visible")){
      header.style.marginBottom = "72px";
    }
  }
}

input.addEventListener('input', updateDatalist);

document.addEventListener('click', (event) => {
  if (!event.target.closest('.select-wrapper')) {
    optionsContainer.classList.remove('visible');
  }

  if (!event.target.closest('.header-nav-search')) {
    customDatalist.classList.remove('show');
  }

  if (
    !headerNavLinks.classList.contains('visible') &&
    !headerNavSearch.classList.contains('visible') &&
    !optionsContainer.classList.contains('visible')
  ) {
    header.style.marginBottom = '24px';
  } else if (
    headerNavLinks.classList.contains('visible') &&
    !headerNavSearch.classList.contains('visible') &&
    !optionsContainer.classList.contains('visible')
  ) {
    header.style.marginBottom = '60px';
  } else if (
    headerNavLinks.classList.contains('visible') &&
    optionsContainer.classList.contains('visible') &&
    !headerNavSearch.classList.contains('visible')
  ) {
    header.style.marginBottom = '148px';
  } else if (
    headerNavSearch.classList.contains('visible') &&
    !headerNavLinks.classList.contains('visible') &&
    !optionsContainer.classList.contains('visible')
  ) {
    header.style.marginBottom = '72px';
  } else if (
    optionsContainer.classList.contains('visible') &&
    !headerNavLinks.classList.contains('visi8ble')
  ) {
    header.style.marginBottom = '100px';
  }
});


                                            