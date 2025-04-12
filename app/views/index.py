import random

from django.http import HttpResponseNotFound
from django.shortcuts import render

from app.models import Work, Category, MainImage

reviews = [
    {
        'name': 'Məmməd R.',
        'desc': 'İşlərinizin keyfiyyəti məni heyran etdi! Çox peşəkar və yaratıcı yanaşmanız var. Gələcək layihələr üçün sizinlə əməkdaşlıq etməyi səbirsizliklə gözləyirəm.',
        'date': 'June 12, 2024'
    }, {
        'name': 'Fərid M.',
        'desc': 'İşləriniz çox ilhamvericidir və hər bir detalda sizin peşəkarlığınız hiss olunur. Mənim layihəmizi mükəmməl həyata keçirdiyiniz üçün təşəkkür edirəm.',
        'date': 'May 30, 2024'
    }, {
        'name': 'Elvin H.',
        'desc': 'Sizinlə işləmək çox rahat və məhsuldar idi. Hər bir təklifi dinləyir və ən yaxşı nəticəni əldə etməyə çalışırsınız. Mən tamamilə razı qaldım.',
        'date': 'May 12, 2024'
    }, {
        'name': 'Orxan T.',
        'desc': 'Əla iş! Çox sürətli və keyfiyyətli xidmət göstərdiniz. Sizinlə işləmək həqiqətən zövq idi. Növbəti layihələrimizdə də sizinlə əməkdaşlıq etmək istərdim.',
        'date': 'Apr 24, 2024'
    }, {
        'name': 'Vüsal Ə.',
        'desc': 'Sizin işinizin keyfiyyəti və vaxtında tamamlanması məni çox məmnun etdi. Sizə gələcək işlərinizdə də uğurlar diləyirəm. Çox sağ olun!',
        'date': 'Apr 16, 2024'
    }, {
        'name': 'Rəşad İ.',
        'desc': 'Sizinlə işləmək çox xoş idi. Peşəkarlığınız və müştəriyə olan hörmətiniz işinizdə hər zaman hiss olunur. Gözəl nəticələr üçün təşəkkür edirəm.',
        'date': 'Apr 2, 2024'
    }, {
        'name': 'Səbuhi Q.',
        'desc': 'İşlərinizə əksərən dəyər verirəm! Sizin peşəkarlığınız və müştəriyə qarşı diqqətiniz gözəl nəticələr əldə etməyimizi təmin edir. Çox təşəkkür edirəm!',
        'date': 'Mar 18, 2024'
    }
]


def index(request):
    random.shuffle(reviews)
    context = {
        "reviews": reviews,
        "main_images": MainImage.objects.order_by("?").all()[:10]
    }
    return render(request, 'index.html', context=context)


def catalog(request):
    context = {
        "works": Work.objects.all(),
        "categories": Category.objects.all(),
    }
    return render(request, 'catalog.html', context=context)


def work_view(request, slug):
    try:
        work = Work.objects.get(slug__iexact=slug)
    except Work.DoesNotExist:
        return HttpResponseNotFound()

    context = {
        "work": work
    }
    return render(request, 'work.html', context=context)
