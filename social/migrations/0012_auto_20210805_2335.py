# Generated by Django 2.2.24 on 2021-08-05 18:05

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('social', '0011_auto_20210805_2320'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='image',
            field=models.ImageField(default='default.jpg', upload_to='images/%Y/%m/%d/'),
        ),
    ]