# Generated by Django 2.0.6 on 2018-09-16 04:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('news', '0003_auto_20180916_0712'),
    ]

    operations = [
        migrations.AlterField(
            model_name='photo',
            name='image',
            field=models.ImageField(upload_to='photo/'),
        ),
    ]
