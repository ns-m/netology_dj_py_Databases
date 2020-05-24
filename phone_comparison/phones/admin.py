from django.contrib import admin
from phones.models import IPhone, Samsung, Xiaomi


@admin.register(IPhone)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Samsung)
class PhoneAdmin(admin.ModelAdmin):
    pass


@admin.register(Xiaomi)
class PhoneAdmin(admin.ModelAdmin):
    pass
