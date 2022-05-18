from django.contrib.auth.models import User
from django.db import models
from django.utils import timezone

from phonenumber_field.modelfields import PhoneNumberField


class Flat(models.Model):
    new_building = models.BooleanField(default=None, null=True)
    created_at = models.DateTimeField(
        'Когда создано объявление',
        default=timezone.now,
        db_index=True
    )
    description = models.TextField('Текст объявления', blank=True)
    price = models.IntegerField('Цена квартиры', db_index=True)
    town = models.CharField(
        'Город, где находится квартира',
        max_length=50,
        db_index=True
    )
    town_district = models.CharField(
        'Район города, где находится квартира',
        max_length=50,
        blank=True,
        help_text='Чертаново Южное',
        db_index=True
    )
    address = models.TextField(
        'Адрес квартиры',
        help_text='ул. Подольских курсантов д.5 кв.4',
        db_index=True
    )
    floor = models.CharField(
        'Этаж',
        max_length=3,
        help_text='Первый этаж, последний этаж, пятый этаж'
    )

    rooms_number = models.IntegerField(
        'Количество комнат в квартире',
        db_index=True
    )
    living_area = models.IntegerField(
        'количество жилых кв.метров',
        null=True,
        blank=True,
        db_index=True
    )

    has_balcony = models.NullBooleanField('Наличие балкона', db_index=True)
    active = models.BooleanField('Активно ли объявление', db_index=True)
    construction_year = models.IntegerField(
        'Год постройки здания',
        null=True,
        blank=True,
        db_index=True
    )
    likes = models.ManyToManyField(
        User,
        verbose_name='Кто лайкнул',
        related_name='flats_liked',
        blank=True
    )

    def __str__(self):
        return f'{self.town}, {self.address} ({self.price}р.)'


class Like(models.Model):
    user = models.ForeignKey(
        User,
        on_delete=models.CASCADE,
        verbose_name='Кто жаловался',
        related_name='complains'
    )
    flat = models.ForeignKey(
        Flat,
        on_delete=models.CASCADE,
        verbose_name='Квартира, на которую жаловались',
        related_name='complains'
    )
    text = models.TextField('Текст жалобы', max_length=1000, blank=True)

    def __str__(self) -> str:
        return self.text.split(' ')[:3]


class Owner(models.Model):
    name = models.CharField('ФИО владельца', max_length=100, db_index=True)
    phone = models.CharField('Номер телефона владельца', max_length=50)
    pure_phone = PhoneNumberField(
        'Нормализованный номер владельца',
        blank=True
    )
    flats = models.ManyToManyField(
        'Flat',
        related_name='owners',
        verbose_name='Квартиры в собственности',
        blank=True,
        db_index=True
    )

    def __str__(self) -> str:
        return self.name
