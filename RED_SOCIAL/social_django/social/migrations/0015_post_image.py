# Generated by Django 3.2.9 on 2021-12-14 22:49

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0014_remove_post_imagen'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='image',
            field=models.ImageField(default='null', upload_to='media/images'),
            preserve_default=False,
        ),
    ]
