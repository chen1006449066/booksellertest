# Generated by Django 3.1.4 on 2020-12-27 14:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bookseller', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vip',
            name='Vphone',
            field=models.PositiveIntegerField(primary_key=True, serialize=False, verbose_name='电话号码'),
        ),
    ]