from bs4 import BeautifulSoup

html_content = """
<div class="review__slider">
    <div class="review__slider-item">
        <div class="slider__body">
            <div class="review__title">
                <h1>Məmməd R.</h1>
                <div class="stars">
                    <span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span>
                </div>
            </div>
            <div class="review__text">
                <p>İşlərinizin keyfiyyəti məni heyran etdi! Çox peşəkar və yaratıcı yanaşmanız var. Gələcək layihələr üçün sizinlə əməkdaşlıq etməyi səbirsizliklə gözləyirəm.</p>
            </div>
            <div class="review__date">
                <h3>June 12, 2024</h3>
            </div>
        </div>
    </div>
    <div class="review__slider-item">
        <div class="slider__body">
            <div class="review__title">
                <h1>Fərid M.</h1>
                <div class="stars">
                    <span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span>
                </div>
            </div>
            <div class="review__text">
                <p>İşləriniz çox ilhamvericidir və hər bir detalda sizin peşəkarlığınız hiss olunur. Mənim layihəmizi mükəmməl həyata keçirdiyiniz üçün təşəkkür edirəm.</p>
            </div>
            <div class="review__date">
                <h3>May 30, 2024</h3>
            </div>
        </div>
    </div>
    <div class="review__slider-item">
        <div class="slider__body">
            <div class="review__title">
                <h1>Elvin H.</h1>
                <div class="stars">
                    <span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span>
                </div>
            </div>
            <div class="review__text">
                <p>Sizinlə işləmək çox rahat və məhsuldar idi. Hər bir təklifi dinləyir və ən yaxşı nəticəni əldə etməyə çalışırsınız. Mən tamamilə razı qaldım.</p>
            </div>
            <div class="review__date">
                <h3>May 12, 2024</h3>
            </div>
        </div>
    </div>
    <div class="review__slider-item">
        <div class="slider__body">
            <div class="review__title">
                <h1>Orxan T.</h1>
                <div class="stars">
                    <span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span>
                </div>
            </div>
            <div class="review__text">
                <p>Əla iş! Çox sürətli və keyfiyyətli xidmət göstərdiniz. Sizinlə işləmək həqiqətən zövq idi. Növbəti layihələrimizdə də sizinlə əməkdaşlıq etmək istərdim.</p>
            </div>
            <div class="review__date">
                <h3>Apr 24, 2024</h3>
            </div>
        </div>
    </div>
    <div class="review__slider-item">
        <div class="slider__body">
            <div class="review__title">
                <h1>Vüsal Ə.</h1>
                <div class="stars">
                    <span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span>
                </div>
            </div>
            <div class="review__text">
                <p>Sizin işinizin keyfiyyəti və vaxtında tamamlanması məni çox məmnun etdi. Sizə gələcək işlərinizdə də uğurlar diləyirəm. Çox sağ olun!</p>
            </div>
            <div class="review__date">
                <h3>Apr 16, 2024</h3>
            </div>
        </div>
    </div>
    <div class="review__slider-item">
        <div class="slider__body">
            <div class="review__title">
                <h1>Rəşad İ.</h1>
                <div class="stars">
                    <span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="/{% static 'img/svg/Vector_star.svg' %}" alt=""></span>
                </div>
            </div>
            <div class="review__text">
                <p>Sizinlə işləmək çox xoş idi. Peşəkarlığınız və müştəriyə olan hörmətiniz işinizdə hər zaman hiss olunur. Gözəl nəticələr üçün təşəkkür edirəm.</p>
            </div>
            <div class="review__date">
                <h3>Apr 2, 2024</h3>
            </div>
        </div>
    </div>
    <div class="review__slider-item">
        <div class="slider__body">
            <div class="review__title">
                <h1>Səbuhi Q.</h1>
                <div class="stars">
                    <span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span><span><img src="{% static 'img/svg/Vector_star.svg' %}" alt=""></span>
                </div>
            </div>
            <div class="review__text">
                <p>İşlərinizə əksərən dəyər verirəm! Sizin peşəkarlığınız və müştəriyə qarşı diqqətiniz gözəl nəticələr əldə etməyimizi təmin edir. Çox təşəkkür edirəm!</p>
            </div>
            <div class="review__date">
                <h3>Mar 18, 2024</h3>
            </div>
        </div>
    </div>
</div>
"""

# Парсим HTML с помощью BeautifulSoup
soup = BeautifulSoup(html_content, 'html.parser')

# Инициализируем список для отзывов
reviews = []

# Находим все элементы отзывов
review_items = soup.find_all('div', class_='review__slider-item')

# Проходимся по каждому отзыву и извлекаем данные
for item in review_items:
    name = item.find('h1').text.strip()
    desc = item.find('div', class_='review__text').p.text.strip()
    date = item.find('div', class_='review__date').h3.text.strip()

    # Создаем словарь для текущего отзыва и добавляем его в список
    review = {
        "name": name,
        "desc": desc,
        "date": date
    }
    reviews.append(review)

print(reviews)