# Generated by Django 3.2.19 on 2023-06-05 23:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0012_auto_20230605_2304'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='question',
            name='content',
        ),
        migrations.AddField(
            model_name='question',
            name='data',
            field=models.JSONField(default=1),
            preserve_default=False,
        ),
    ]
