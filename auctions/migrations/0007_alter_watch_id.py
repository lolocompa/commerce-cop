# Generated by Django 4.1.6 on 2023-11-27 21:57

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0006_watch'),
    ]

    operations = [
        migrations.AlterField(
            model_name='watch',
            name='id',
            field=models.AutoField(auto_created=True, primary_key=True, serialize=False),
        ),
    ]
