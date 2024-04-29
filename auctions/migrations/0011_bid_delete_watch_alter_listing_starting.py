# Generated by Django 4.1.6 on 2023-11-27 22:58

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0010_alter_user_id'),
    ]

    operations = [
        migrations.CreateModel(
            name='bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.DecimalField(decimal_places=2, max_digits=5)),
                ('bidder', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.DeleteModel(
            name='watch',
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='bidprice', to='auctions.bid'),
        ),
    ]