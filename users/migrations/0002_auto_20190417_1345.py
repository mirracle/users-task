# Generated by Django 2.2 on 2019-04-17 13:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('users', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='userid',
            name='name',
            field=models.CharField(blank=True, max_length=10, null=True, verbose_name='Name for ID'),
        ),
        migrations.AlterField(
            model_name='userid',
            name='value',
            field=models.CharField(blank=True, max_length=50, null=True, verbose_name='Value of ID'),
        ),
    ]
