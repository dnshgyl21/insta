# Generated by Django 2.2.2 on 2020-11-22 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_upload', '0006_auto_20201122_1943'),
    ]

    operations = [
        migrations.AlterField(
            model_name='upload',
            name='image',
            field=models.ImageField(upload_to='media/images/'),
        ),
    ]
