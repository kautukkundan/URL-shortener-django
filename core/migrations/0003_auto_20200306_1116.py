# Generated by Django 3.0 on 2020-03-06 11:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0002_auto_20200306_1106'),
    ]

    operations = [
        migrations.AlterField(
            model_name='url',
            name='clicks',
            field=models.IntegerField(default=0),
        ),
    ]
