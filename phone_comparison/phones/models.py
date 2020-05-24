from django.db import models


class Phone(models.Model):
    name = models.CharField(max_length=100)
    price = models.IntegerField()
    os = models.CharField(max_length=100)
    ram = models.CharField(max_length=100)
    release_date = models.DateField()
    lte_exists = models.NullBooleanField()
    sim_count = models.IntegerField()
    display = models.CharField(max_length=100)
    memory_count = models.CharField(max_length=100)
    bluetooth = models.NullBooleanField()
    color = models.CharField(max_length=100)

    def __str__(self):
        return self.name

    class Meta:
        abstract = True


class IPhone(Phone):
    screen_security = models.CharField(max_length=100)
    dictofon = models.NullBooleanField()

    class Meta:
        db_table = 'iphone'
        verbose_name = 'Iphone'
        verbose_name_plural = 'Iphones'


class Samsung(Phone):
    micro_sd = models.NullBooleanField()
    micro_sd_memory = models.CharField(max_length=100)

    class Meta:
        db_table = 'samsung'
        verbose_name = 'Samsung'
        verbose_name_plural = 'Samsungs'


class Xiaomi(Phone):
    monobrov = models.NullBooleanField()

    class Meta:
        db_table = 'xiaomi'
        verbose_name = 'Xiaomi'
        verbose_name_plural = 'Xiaomis'
