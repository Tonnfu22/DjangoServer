# Generated by Django 3.1.5 on 2021-05-27 15:37

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0030_profit_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profit',
            name='wallet',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.wallet'),
        ),
    ]