# Generated by Django 3.1.4 on 2021-01-05 04:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0004_listing_price'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='image',
            field=models.ImageField(blank=True, default='default.jpg', upload_to='images'),
        ),
    ]
