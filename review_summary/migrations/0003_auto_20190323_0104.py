# Generated by Django 2.1.7 on 2019-03-22 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('review_summary', '0002_remove_restaurant_restaurantlocation'),
    ]

    operations = [
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantCostForTwo',
            field=models.CharField(max_length=10),
        ),
        migrations.AlterField(
            model_name='restaurant',
            name='restaurantRating',
            field=models.CharField(max_length=10),
        ),
    ]