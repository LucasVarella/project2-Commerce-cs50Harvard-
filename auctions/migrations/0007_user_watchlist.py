# Generated by Django 4.1.3 on 2022-12-04 16:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_rename_image_auction_image_url'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='watchlist',
            field=models.ManyToManyField(related_name='watch', to='auctions.auction'),
        ),
    ]
