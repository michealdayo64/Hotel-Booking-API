# Generated by Django 2.2.8 on 2022-01-26 02:42

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0002_auto_20220125_1834'),
    ]

    operations = [
        migrations.AddField(
            model_name='room',
            name='price',
            field=models.FloatField(blank=True, default=0.0, null=True),
        ),
    ]