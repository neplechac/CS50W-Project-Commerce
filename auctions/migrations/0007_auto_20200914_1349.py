# Generated by Django 3.0.8 on 2020-09-14 11:49

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_listing_users_watching'),
    ]

    operations = [
        migrations.RenameField(
            model_name='category',
            old_name='category',
            new_name='name',
        ),
    ]
