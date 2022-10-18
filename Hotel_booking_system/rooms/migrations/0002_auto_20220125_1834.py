# Generated by Django 2.2.8 on 2022-01-26 02:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rooms', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='room',
            name='room_images',
        ),
        migrations.AddField(
            model_name='room',
            name='image1',
            field=models.ImageField(blank=True, null=True, upload_to='room'),
        ),
        migrations.AddField(
            model_name='room',
            name='image2',
            field=models.ImageField(blank=True, null=True, upload_to='room'),
        ),
        migrations.AddField(
            model_name='room',
            name='image3',
            field=models.ImageField(blank=True, null=True, upload_to='room'),
        ),
        migrations.AddField(
            model_name='room',
            name='image4',
            field=models.ImageField(blank=True, null=True, upload_to='room'),
        ),
        migrations.AddField(
            model_name='room',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='room'),
        ),
        migrations.DeleteModel(
            name='RoomImage',
        ),
    ]