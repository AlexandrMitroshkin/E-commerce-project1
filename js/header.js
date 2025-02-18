                                            // элеметнты выпадающего списка

let header = document.getElementById("header");
let selectedOptionArrow = document.querySelector(".selected-option-arrow");
const selectedOption = document.getElementById('selected-option');
const optionsContainer = document.querySelector('.options');
const optionsList = document.querySelectorAll('.option');

                                            // элементы search

const input = document.getElementById('header-nav-input');
const customDatalist = document.getElementById('custom-datalist');
let headerNavSearch = document.querySelector(".header-nav-search");

const data = {
  "thing1": "https://trychatgpt.ru/",
  "thing2": "#",
  "thing3": "#",
  "thing4": "#",
  "thing5": "#",
  "thing6": "#",
  "thing7": "#",
  "thing8": "#",
  "thing9": "#",
  "thing10": "#"
};


                                            // реализация выпадающего списка

function toggleOptions() {
  if (optionsContainer.classList.contains('visible')) {
    optionsContainer.classList.remove('visible');
    selectedOptionArrow.classList.add("notInverted");
    if (!customDatalist.classList.contains('show')) {
      header.style.marginBottom = "24px";
    }
  } else {
    optionsContainer.classList.add('visible');
    header.style.marginBottom = "100px";
    selectedOptionArrow.classList.remove("notInverted");
  }
}

selectedOption.addEventListener('click', toggleOptions);
document.addEventListener('click', (event) => {
    if (!event.target.closest('.select-wrapper')) {
        optionsContainer.classList.remove('visible');
      if (!customDatalist.classList.contains('show')) {
        header.style.marginBottom = "24px";
      }
    }
  });

                                                        // реализация search
                                                        
  function updateDatalist() {
  const inputValue = input.value.toLowerCase();
  const filteredData = Object.keys(data).filter(item => {
    return item.toLowerCase().includes(inputValue);
  });

  customDatalist.innerHTML = '';

  if (inputValue && filteredData.length > 0) {
    filteredData.forEach(item => {
      const option = document.createElement('div');
      option.textContent = item;
      option.setAttribute('data-href', data[item]);
      option.addEventListener('click', () => {
        input.value = item;
        customDatalist.classList.remove('show');
        if (!optionsContainer.classList.contains('visible')) {
          header.style.marginBottom = "24px";
        }
        window.location.href = data[item];
      });
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
    if (!optionsContainer.classList.contains('visible')) {
      header.style.marginBottom = "24px";
    }
  }
}

input.addEventListener('input', updateDatalist);

document.addEventListener('click', (event) => {
  if (!event.target.closest('.header-nav-search')) {
    customDatalist.classList.remove('show');
    if (!optionsContainer.classList.contains('visible')) {
      header.style.marginBottom = "24px";
    }
  }
});





function updateDatalist() {
    const inputValue = input.value.toLowerCase();
    const filteredData = Object.keys(data).filter(item => {
      return item.toLowerCase().includes(inputValue);
    });
  
    customDatalist.innerHTML = '';
  
    if (inputValue && filteredData.length > 0) {
      filteredData.forEach(item => {
        const option = document.createElement('div');
        option.textContent = item;
        option.setAttribute('data-href', data[item]);
        option.addEventListener('click', () => {
          input.value = item;
          customDatalist.classList.remove('show');
          if (!optionsContainer.classList.contains('visible')) {
            header.style.marginBottom = "24px";
          }
          window.location.href = data[item];
        });
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
      if (!optionsContainer.classList.contains('visible')) {
        header.style.marginBottom = "24px";
      }
    }
  }
  
input.addEventListener('input', updateDatalist);
  
document.addEventListener('click', (event) => {
if (!event.target.closest('.header-nav-search')) {
    customDatalist.classList.remove('show');
    if (!optionsContainer.classList.contains('visible')) {
    header.style.marginBottom = "24px";
    }
}
});