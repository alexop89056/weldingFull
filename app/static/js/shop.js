$(document).ready(function() {
    $('.order').on('click', function() {
        $('.order__form').addClass('open');
        $('body').addClass('lock');
    });
    $('.shop__element').on('click', function() {
        $('.popup').addClass('open');
        $('body').addClass('lock');
    });
    $('.close').on('click', function () {
        $('.order__form').removeClass('open');
        $('body').removeClass('lock');
        $('.popup').removeClass('open');
    });

    $('.product__page-slider').slick({
        slidesToShow: 1,
        slidesToScroll: 1,
        arrows: false,
        fade: true,
        asNavFor: '.page__slider-for'
      });
    $('.page__slider-for').slick({
        slidesToShow: 3,
        slidesToScroll: 1,
        asNavFor: '.product__page-slider',
        dots: false,
        centerMode: true,
        focusOnSelect: true,
        responsive: [
            {
                breakpoint: 767,
                settings: {
                    slidesToShow: 2
                }
            }
        ]
    });
});

// Получаем ссылки на элементы DOM для первого меню
const dropdownBtn1 = document.querySelectorAll('.dropbtn')[0];
const dropdownContent1 = document.querySelectorAll('.dropdown-content')[0];

// Получаем ссылки на элементы DOM для второго меню
const dropdownBtn2 = document.querySelectorAll('.dropbtn')[1];
const dropdownContent2 = document.querySelectorAll('.dropdown-content')[1];

// Функция для показа выпадающего меню
function showDropdownContent(btn, content) {
    content.classList.add('show');
}

// Функция для скрытия выпадающего меню
function hideDropdownContent(content) {
    content.classList.remove('show');
}

// Обработчики событий для первого меню
dropdownBtn1.addEventListener('mouseenter', () => {
    showDropdownContent(dropdownBtn1, dropdownContent1);
});

dropdownContent1.addEventListener('mouseleave', () => {
    hideDropdownContent(dropdownContent1);
});

// Обработчики событий для второго меню
dropdownBtn2.addEventListener('mouseenter', () => {
    showDropdownContent(dropdownBtn2, dropdownContent2);
});

dropdownContent1.addEventListener('mouseleave', () => {
    hideDropdownContent(dropdownContent2);
});

// Скрываем выпадающее меню при клике вне него
document.addEventListener('click', (event) => {
    if (!event.target.matches('.dropbtn')) {
        hideDropdownContent(dropdownContent1);
        hideDropdownContent(dropdownContent2);
    }
});
