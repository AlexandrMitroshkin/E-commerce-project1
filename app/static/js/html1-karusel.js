let currentIndex = 0;

function moveCarousel(direction) {
    const container = document.querySelector('.carousel-container');
    const groups = document.querySelectorAll('.review-group');
    const totalGroups = groups.length;

    currentIndex += direction;

    if (currentIndex < 0) {
        currentIndex = totalGroups - 1;
    } else if (currentIndex >= totalGroups) {
        currentIndex = 0;
    }

    const offset = -currentIndex * 100;
    container.style.transform = `translateX(${offset}%)`;
}