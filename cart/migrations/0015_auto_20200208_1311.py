# Generated by Django 3.0.2 on 2020-02-08 13:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cart', '0014_auto_20200208_1311'),
    ]

    operations = [
        migrations.AlterField(
            model_name='history',
            name='address',
            field=models.CharField(default='kek', max_length=150),
        ),
    ]