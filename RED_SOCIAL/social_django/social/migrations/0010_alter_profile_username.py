# Generated by Django 3.2.9 on 2021-12-09 23:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0009_alter_profile_username'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='username',
            field=models.CharField(default='nata', max_length=255),
            preserve_default=False,
        ),
    ]