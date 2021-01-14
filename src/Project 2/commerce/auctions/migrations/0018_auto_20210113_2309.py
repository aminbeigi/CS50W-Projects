# Generated by Django 3.1.4 on 2021-01-13 12:09

from decimal import Decimal
import django.core.validators
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0017_auto_20210113_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bid',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
        migrations.AlterField(
            model_name='listing',
            name='price',
            field=models.DecimalField(decimal_places=2, default=0.0, max_digits=8, validators=[django.core.validators.MinValueValidator(Decimal('0.01'))]),
        ),
    ]