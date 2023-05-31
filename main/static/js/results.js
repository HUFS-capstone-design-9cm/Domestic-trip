
let currentSlide = 0;
let slideCount = document.getElementsByClassName('spot-slide').length;

function showSlide(direction) {
    let slides = document.getElementsByClassName('spot-slide');
    slides[currentSlide].style.display = 'none';
    
    if (direction === 'prev') {
        currentSlide = (currentSlide - 1 + slideCount) % slideCount;
    } else if (direction === 'next') {
        currentSlide = (currentSlide + 1) % slideCount;
    }
    
    slides[currentSlide].style.display = 'block';
}