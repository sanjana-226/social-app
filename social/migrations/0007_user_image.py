# Generated by Django 2.2.24 on 2021-08-05 17:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0006_auto_20210804_2231'),
    ]

    operations = [
        migrations.AddField(
            model_name='user',
            name='image',
            field=models.ImageField(default='images/default.jpg', upload_to='profile_pics'),
        ),
    ]
