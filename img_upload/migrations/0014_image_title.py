# Generated by Django 2.2.2 on 2020-11-23 15:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('img_upload', '0013_auto_20201123_1535'),
    ]

    operations = [
        migrations.AddField(
            model_name='image',
            name='title',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
    ]