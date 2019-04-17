from __future__ import unicode_literals
from django.db import models
from django.utils.translation import ugettext_lazy as _
import uuid

MALE = 'male'
FEMALE = 'female'
GENDERS = (
    (MALE, _('Мужской')),
    (FEMALE, _('Женский'))
)


class User(models.Model):
    gender = models.CharField(max_length=10, choices=GENDERS, verbose_name='Пол')
    email = models.EmailField(max_length=254, verbose_name='Электронный почта')
    dob = models.DateTimeField(auto_now=False, auto_now_add=False, verbose_name='Дата рожадения')
    registered = models.DateTimeField(auto_now_add=False, auto_now=False, verbose_name='Дата регистрции')
    phone = models.CharField(max_length=20, verbose_name='Номер телефона')
    cell = models.CharField(max_length=20, verbose_name='Номер сотового телефона')
    nat = models.CharField(max_length=10, verbose_name='Национальность')


class UserLogin(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='login')
    uuid = models.UUIDField(default=uuid.uuid4, verbose_name='uuid', editable=False, primary_key=False)
    username = models.CharField(max_length=50, verbose_name='Логин')
    password = models.CharField(max_length=100, verbose_name='Пароль')
    salt = models.CharField(max_length=50, verbose_name='salt')
    md5 = models.CharField(max_length=100, verbose_name='md5')
    md5_chars = models.CharField(max_length=100, verbose_name='md5_chars', blank=True, null=True)
    md5_digit = models.CharField(max_length=100, verbose_name='md5_digit', blank=True, null=True)
    sha1 = models.CharField(max_length=100, verbose_name='sha1')
    sha1_chars = models.CharField(max_length=100, verbose_name='sha1_chars', blank=True, null=True)
    sha1_digit = models.CharField(max_length=100, verbose_name='sha1_digit', blank=True, null=True)
    sha256 = models.CharField(max_length=100, verbose_name='sha256')
    sha256_chars = models.CharField(max_length=100, verbose_name='sha256_chars', blank=True, null=True)
    sha256_digit = models.CharField(max_length=100, verbose_name='sha256_digit', blank=True, null=True)


class UserId(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='id_user')
    name = models.CharField(max_length=10, verbose_name='Name for ID', blank=True, null=True)
    value = models.CharField(max_length=50, verbose_name='Value of ID', blank=True, null=True)


class UserPicture(models.Model):
    # there are must be an ImageFields in real project
    large = models.URLField(max_length=300, verbose_name='XL фото')
    medium = models.URLField(max_length=300, verbose_name='M фото')
    thumbnail = models.URLField(max_length=300, verbose_name='XS фото')
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='picture', blank=True, null=True)


class UserName(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='name')
    title = models.CharField(max_length=20, verbose_name='Обращение')
    first = models.CharField(max_length=20, verbose_name='Имя')
    last = models.CharField(max_length=20, verbose_name='Фамилия')


class UserLocation(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, related_name='location')
    street = models.CharField(max_length=100, verbose_name='Улица')
    city = models.CharField(max_length=50, verbose_name='Город')
    state = models.CharField(max_length=50, verbose_name='Область')
    postcode = models.CharField(max_length=50, verbose_name='Почтовый индекс')


class LocationCoordinates(models.Model):
    location = models.OneToOneField(UserLocation, on_delete=models.CASCADE, related_name='coordinates')
    latitude = models.FloatField(verbose_name='Широта')
    longitude = models.FloatField(verbose_name='Долгота')


class LocationTimezone(models.Model):
    location = models.OneToOneField(UserLocation, on_delete=models.CASCADE, related_name='timezone')
    offset = models.CharField(max_length=10, verbose_name='Часовой пояс')
    description = models.CharField(max_length=400, verbose_name='Города часовго пояса')
