# Generated by Django 3.0.3 on 2020-02-19 16:58

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pp', '0007_auto_20200219_1653'),
    ]

    operations = [
        migrations.AddField(
            model_name='pizza',
            name='created_at',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]