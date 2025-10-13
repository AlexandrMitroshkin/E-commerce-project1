let currentIndex = 0;
let isMobileView = window.innerWidth < 768;

// Инициализация карусели
function initCarousel() {
    checkViewport();
    
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(checkViewport, 150);
    });
    
    updateCarouselPosition();
}

// Проверяем тип устройства и адаптируем структуру
function checkViewport() {
    const oldView = isMobileView;
    isMobileView = window.innerWidth < 768;
    
    if (oldView !== isMobileView) {
        currentIndex = 0;
        if (isMobileView) {
            adaptForMobile();
        } else {
            restoreForDesktop();
        }
        updateCarouselPosition();
    }
}

// Адаптируем карусель для мобильных устройств
function adaptForMobile() {
    const container = document.querySelector('.carousel-container');
    const allReviewItems = document.querySelectorAll('.Reviews-item');
    
    // Сохраняем оригинальную структуру для восстановления
    if (!container.desktopHTML) {
        container.desktopHTML = container.innerHTML;
    }
    
    // Очищаем контейнер
    container.innerHTML = '';
    
    // Создаем отдельные слайды для каждого отзыва
    allReviewItems.forEach((item) => {
        const slide = document.createElement('li');
        slide.className = 'review-group-mobile';
        slide.style.minWidth = '100%';
        slide.style.flexShrink = '0';
        
        const clonedItem = item.cloneNode(true);
        slide.appendChild(clonedItem);
        container.appendChild(slide);
    });
}

// Восстанавливаем десктопную структуру
function restoreForDesktop() {
    const container = document.querySelector('.carousel-container');
    if (container.desktopHTML) {
        container.innerHTML = container.desktopHTML;
    }
}

// Основная функция перемещения
function moveCarousel(direction) {
    const container = document.querySelector('.carousel-container');
    
    if (isMobileView) {
        // На мобилке листаем по отдельным отзывам
        const mobileSlides = document.querySelectorAll('.review-group-mobile');
        const totalSlides = mobileSlides.length;
        
        if (totalSlides === 0) return;
        
        currentIndex += direction;
        
        // Зацикливание для мобильного режима
        if (currentIndex < 0) {
            currentIndex = totalSlides - 1;
        } else if (currentIndex >= totalSlides) {
            currentIndex = 0;
        }
    } else {
        // На десктопе листаем по группам
        const groups = document.querySelectorAll('.review-group');
        const totalGroups = groups.length;
        
        if (totalGroups === 0) return;
        
        currentIndex += direction;
        
        // Зацикливание для десктопного режима
        if (currentIndex < 0) {
            currentIndex = totalGroups - 1;
        } else if (currentIndex >= totalGroups) {
            currentIndex = 0;
        }
    }
    
    updateCarouselPosition();
}

// Обновляем позицию карусели
function updateCarouselPosition() {
    const container = document.querySelector('.carousel-container');
    const offset = -currentIndex * 100;
    container.style.transform = `translateX(${offset}%)`;
}

// Инициализация при загрузке страницы
document.addEventListener('DOMContentLoaded', function() {
    // Сразу адаптируем под текущий размер экрана
    if (window.innerWidth < 768) {
        adaptForMobile();
    }
    initCarousel();
});