# Generated by Django 3.1.5 on 2021-05-18 08:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0012_trader_referral_bonus'),
    ]

    operations = [
        migrations.AddField(
            model_name='trader',
            name='password',
            field=models.CharField(max_length=100, null=True),
        ),
    ]
