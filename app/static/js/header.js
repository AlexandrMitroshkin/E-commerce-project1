const header = document.getElementById("header");
const headerRegister = document.querySelector(".header-register");
const headerNavMore = document.querySelector(".header-nav-more");
const headerNavLinks = document.querySelector(".header-nav-links");
const headerNavSearch = document.querySelector(".header-nav-search");
const MagnifyingGlassButton = document.querySelector(".Magnifying_glass-button");
const input = document.getElementById('header-nav-input');
const customDatalist = document.getElementById('custom-datalist');
const selectedOption = document.getElementById('selected-option');
const optionsContainer = document.querySelector('.options');
const selectedOptionArrow = document.querySelector(".selected-option-arrow");


document.querySelector(".header-register-close")?.addEventListener('click', () => {
    headerRegister.style.display = "none";
    header.style.paddingTop = "10px";
    header.style.height = "48px";
});


headerNavMore?.addEventListener('click', () => {
    headerNavSearch.classList.remove("visible");
    headerNavLinks.classList.toggle("visible");
    headerNavMore.classList.toggle("inverted");
    updateMargins();
});


MagnifyingGlassButton?.addEventListener('click', () => {
    headerNavSearch.classList.toggle("visible");
    if (headerNavLinks.classList.contains("visible")) {
        headerNavLinks.classList.remove("visible");
        headerNavMore.classList.remove("inverted");
    }
    updateMargins();
});

selectedOption?.addEventListener('click', () => {
    optionsContainer.classList.toggle("visible");
    selectedOptionArrow?.classList.toggle("notInverted");
    updateMargins();
});


input?.addEventListener('input', async () => {
    const searchTerm = input.value.trim();

    try {
        const response = await fetch(`/search-products?q=${encodeURIComponent(searchTerm)}`);
        const products = await response.json();
        
        customDatalist.innerHTML = '';
        
        if (products.length === 0) {
            const noResults = document.createElement('div');
            noResults.className = 'no-results';
            noResults.textContent = 'Товары не найдены';
            customDatalist.appendChild(noResults);
        } else {
            products.forEach(product => {
                const resultItem = document.createElement('a');
                resultItem.className = 'search-result-item';
                resultItem.href = product.url;
                resultItem.innerHTML = `
                    <div class="search-item-info">
                        <span class="search-product-name">${product.name}</span>
                        <span class="search-product-category">${product.category}</span>
                    </div>
                    <span class="search-product-price">$${product.price.toFixed(2)}</span>
                `;
                
                resultItem.addEventListener('click', (e) => {
                    input.value = product.name;
                    customDatalist.classList.remove('show');
                    updateMargins();
                });
                
                customDatalist.appendChild(resultItem);
            });
        }
        
        customDatalist.classList.add('show');
        updateMargins();
        
    } catch (error) {
        console.error('Ошибка поиска:', error);
        customDatalist.classList.remove('show');
        updateMargins();
    }
});


document.addEventListener('click', (event) => {
    if (!event.target.closest('.select-wrapper')) {
        optionsContainer.classList.remove("visible");
        selectedOptionArrow?.classList.add("notInverted");
    }
    
    if (!event.target.closest('.header-nav-search')) {
        customDatalist.classList.remove('show');
    }
    
    updateMargins();
});


function updateMargins() {
    if (!header) return;

    let margin = 24;

    if (headerNavLinks.classList.contains("visible")) margin += 36;
    if (headerNavSearch.classList.contains("visible")) margin += 12;
    if (optionsContainer.classList.contains("visible")) margin += 100;

    if (customDatalist.classList.contains('show')) {
        margin += 2 * 40
    }
    
    header.style.marginBottom = margin + "px";
}

document.addEventListener('DOMContentLoaded', () => {
    updateMargins();

    if (input && input.value.trim().length >= 2) {
        input.dispatchEvent(new Event('input'));
    }

    if (optionsContainer) {
        const categories = {
            'men': 'Men', 'women': 'Women', 'casual': 'Casual','gym': 'Gym'
          };
        
        optionsContainer.innerHTML = '';
        Object.entries(categories).forEach(([slug, name]) => {
            const option = document.createElement('a');
            option.className = 'option';
            option.textContent = name;
            option.href = `/category/${slug}`;
            optionsContainer.appendChild(option);
        });
    }
});