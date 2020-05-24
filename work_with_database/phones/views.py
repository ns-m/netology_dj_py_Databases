from django.shortcuts import render, reverse
from django.core.exceptions import ObjectDoesNotExist
from django.http import HttpResponseNotFound

from phones.models import Phone


def home_view(request):
    template_name = 'home.html'
    pages = {
        'Главная страница': reverse('home_view'),
        'Показать каталог телефонов': reverse('catalog')
    }
    context = {
        'pages': pages
    }
    return render(request, template_name, context)

def show_catalog(request):
    template = 'catalog.html'

    sort = request.GET.get('sort', '')
    if sort == 'name':
        phones = Phone.objects.order_by("name")
    elif sort == 'minprice':
        phones = Phone.objects.order_by("price")
    elif sort == 'maxprice':
        phones = Phone.objects.order_by("-price")
    else:
        phones = Phone.objects.all()
    context = {'phones': phones}
    return render(request, template, context)


def show_product(request, slug):
    template = 'product.html'

    try:
        phone = Phone.objects.get(slug=slug)
    except ObjectDoesNotExist:
        return HttpResponseNotFound("Phone does not exist")

    context = {'phone': phone}

    return render(request, template, context)

