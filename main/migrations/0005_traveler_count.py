# Generated by Django 3.2.19 on 2023-05-25 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0004_auto_20230517_0513'),
    ]

    operations = [
        migrations.AddField(
            model_name='traveler',
            name='count',
            field=models.IntegerField(default=0),
        ),
    ]