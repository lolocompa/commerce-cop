# Generated by Django 4.1.6 on 2023-11-26 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_listing_user_alter_listing_category_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='user',
            field=models.CharField(max_length=50),
        ),
    ]
