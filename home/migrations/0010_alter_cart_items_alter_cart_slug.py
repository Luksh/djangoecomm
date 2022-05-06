# Generated by Django 4.0.4 on 2022-05-06 13:18

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0009_cart_total'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cart',
            name='items',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='home.product'),
        ),
        migrations.AlterField(
            model_name='cart',
            name='slug',
            field=models.CharField(max_length=400),
        ),
    ]
