from django.shortcuts import render
from phones.models import IPhone, Samsung, Xiaomi


def show_catalog(request):
    template = 'catalog.html'

    iphone = IPhone.objects.all()
    samsung = Samsung.objects.all()
    xiaomi = Xiaomi.objects.all()
    phones = [iphone, samsung, xiaomi]
    context = {
                'phones': phones
    }

    return render(
        request,
        template,
        context
    )
