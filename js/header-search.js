const input = document.getElementById('header-nav-input');
const customDatalist = document.getElementById('custom-datalist');
let headerNavSearch = document.querySelector(".header-nav-search");
let siteHat = document.getElementById("header");

// Словарь: ключ - текст, значение - ссылка
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

function updateDatalist() {
  const inputValue = input.value.toLowerCase();
  // Фильтруем ключи словаря
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
        siteHat.style.marginBottom = "24px";
        window.location.href = data[item];
      });
      customDatalist.appendChild(option);
    });

    switch (filteredData.length) {
      case 1:
        siteHat.style.marginBottom = "61.5px";
        break;
      case 2:
        siteHat.style.marginBottom = "99px";
        break;
      case 3:
        siteHat.style.marginBottom = "136.5px";
        break;
      default:
        siteHat.style.marginBottom = "174px";
        break;
    }

    customDatalist.classList.add('show');
  } else {
    customDatalist.classList.remove('show');
    siteHat.style.marginBottom = "24px";
  }
}

input.addEventListener('input', updateDatalist);

document.addEventListener('click', (event) => {
  if (!event.target.closest('.header-nav-search')) {
    customDatalist.classList.remove('show');
    siteHat.style.marginBottom = "24px";
  }
});









