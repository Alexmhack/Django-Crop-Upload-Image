# Generated by Django 2.1.2 on 2019-01-06 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('photos', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(height_field='image_heigth', upload_to='%Y/%m/%d/', width_field='image_width'),
        ),
    ]
