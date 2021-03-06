# Generated by Django 2.2 on 2019-04-16 10:01

from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('gender', models.CharField(choices=[('male', 'Мужской'), ('female', 'Женский')], max_length=10, verbose_name='Пол')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронный почта')),
                ('dob', models.DateTimeField(verbose_name='Дата рожадения')),
                ('registered', models.DateTimeField(verbose_name='Дата регистрции')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('cell', models.CharField(max_length=20, verbose_name='Номер сотового телефона')),
                ('nat', models.CharField(max_length=10, verbose_name='Национальность')),
            ],
        ),
        migrations.CreateModel(
            name='UserPicture',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('large', models.URLField(max_length=300, verbose_name='XL фото')),
                ('medium', models.URLField(max_length=300, verbose_name='M фото')),
                ('thumbnail', models.URLField(max_length=300, verbose_name='XS фото')),
            ],
        ),
        migrations.CreateModel(
            name='UserName',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, verbose_name='Обращение')),
                ('first', models.CharField(max_length=20, verbose_name='Имя')),
                ('last', models.CharField(max_length=20, verbose_name='Фамилия')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='name', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserLogin',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, verbose_name='uuid')),
                ('username', models.CharField(max_length=50, verbose_name='Логин')),
                ('password', models.CharField(max_length=100, verbose_name='Пароль')),
                ('salt', models.CharField(max_length=50, verbose_name='salt')),
                ('md5', models.CharField(max_length=100, verbose_name='md5')),
                ('sha1', models.CharField(max_length=100, verbose_name='sha1')),
                ('sha256', models.CharField(max_length=100, verbose_name='sha256')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='users.User', verbose_name='login')),
            ],
        ),
        migrations.CreateModel(
            name='UserLocation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('street', models.CharField(max_length=100, verbose_name='Улица')),
                ('city', models.CharField(max_length=50, verbose_name='Город')),
                ('state', models.CharField(max_length=50, verbose_name='Область')),
                ('postcode', models.CharField(max_length=50, verbose_name='Почтовый индекс')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='location', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='UserId',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=10, verbose_name='Name for ID')),
                ('value', models.CharField(max_length=50, verbose_name='Value of ID')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='id_user', to='users.User')),
            ],
        ),
        migrations.CreateModel(
            name='LocationTimezone',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('offset', models.CharField(max_length=10, verbose_name='Часовой пояс')),
                ('description', models.CharField(max_length=400, verbose_name='Города часовго пояса')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='timezone', to='users.UserLocation')),
            ],
        ),
        migrations.CreateModel(
            name='LocationCoordinates',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('latitude', models.FloatField(verbose_name='Широта')),
                ('longitude', models.FloatField(verbose_name='Долгота')),
                ('location', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='coordinates', to='users.UserLocation')),
            ],
        ),
    ]
