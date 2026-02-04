let currentIndex = 0;
let isMobileView = window.innerWidth < 768;

function initCarousel() {
    checkViewport();
    
    let resizeTimeout;
    window.addEventListener('resize', function() {
        clearTimeout(resizeTimeout);
        resizeTimeout = setTimeout(checkViewport, 150);
    });
    
    updateCarouselPosition();
}

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

function adaptForMobile() {
    const container = document.querySelector('.carousel-container');
    const allReviewItems = document.querySelectorAll('.Reviews-item');

    if (!container.desktopHTML) {
        container.desktopHTML = container.innerHTML;
    }

    container.innerHTML = '';

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

function restoreForDesktop() {
    const container = document.querySelector('.carousel-container');
    if (container.desktopHTML) {
        container.innerHTML = container.desktopHTML;
    }
}

function moveCarousel(direction) {
    const container = document.querySelector('.carousel-container');
    
    if (isMobileView) {

        const mobileSlides = document.querySelectorAll('.review-group-mobile');
        const totalSlides = mobileSlides.length;
        
        if (totalSlides === 0) return;
        
        currentIndex += direction;

        if (currentIndex < 0) {
            currentIndex = totalSlides - 1;
        } else if (currentIndex >= totalSlides) {
            currentIndex = 0;
        }
    } else {

        const groups = document.querySelectorAll('.review-group');
        const totalGroups = groups.length;
        
        if (totalGroups === 0) return;
        
        currentIndex += direction;

        if (currentIndex < 0) {
            currentIndex = totalGroups - 1;
        } else if (currentIndex >= totalGroups) {
            currentIndex = 0;
        }
    }
    
    updateCarouselPosition();
}

function updateCarouselPosition() {
    const container = document.querySelector('.carousel-container');
    const offset = -currentIndex * 100;
    container.style.transform = `translateX(${offset}%)`;
}

document.addEventListener('DOMContentLoaded', function() {
    if (window.innerWidth < 768) {
        adaptForMobile();
    }
    initCarousel();
});