# Generated by Django 5.0.4 on 2024-04-25 10:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='product',
            options={'verbose_name': 'Товар', 'verbose_name_plural': 'Товары'},
        ),
        migrations.AlterField(
            model_name='product',
            name='price',
            field=models.PositiveBigIntegerField(verbose_name='Цена'),
        ),
    ]
