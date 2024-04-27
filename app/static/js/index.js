const burger = document.querySelector('.header__burger');
const header_menu_list = document.querySelector('.header__menu');
const body = document.querySelector('body');

burger.addEventListener('click', function (event){
    burger.classList.toggle('active')
    header_menu_list.classList.toggle('active');
    body.classList.toggle('lock');
});

$(document).ready(function() {
    $('.order').on('click', function() {
        $('.order__form').addClass('open');
        $('body').addClass('lock');
    });
    $('.close').on('click', function () {
        $('.order__form').removeClass('open');
        $('body').removeClass('lock');
    });


    $('.products__slider').slick({
        dots: true,
        slidesToShow: 4,
        adaptiveHeight: true,

        responsive: [
            {
                breakpoint: 993,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 690,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });
    $('.review__slider').slick({
        dots: true,
        slidesToShow: 3,
        adaptiveHeight: true,

        responsive: [
            {
                breakpoint: 993,
                settings: {
                    slidesToShow: 2
                }
            },
            {
                breakpoint: 690,
                settings: {
                    slidesToShow: 1
                }
            }
        ]
    });
});
