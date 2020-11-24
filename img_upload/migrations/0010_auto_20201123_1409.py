# Generated by Django 2.2.2 on 2020-11-23 14:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('img_upload', '0009_auto_20201123_1408'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='add_image',
            name='image',
        ),
        migrations.AddField(
            model_name='add_image',
            name='title',
            field=models.TextField(default=0),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='add_image',
            name='img_new',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='img_upload.Upload'),
        ),
    ]
