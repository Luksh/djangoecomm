# Generated by Django 4.0.4 on 2022-04-24 03:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0005_product_slug'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='description',
            field=models.TextField(blank=True),
        ),
    ]