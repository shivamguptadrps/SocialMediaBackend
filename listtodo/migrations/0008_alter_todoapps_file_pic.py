# Generated by Django 3.2.10 on 2021-12-29 09:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('listtodo', '0007_auto_20211229_0825'),
    ]

    operations = [
        migrations.AlterField(
            model_name='todoapps',
            name='file_pic',
            field=models.ImageField(upload_to='listtodo/static/img'),
        ),
    ]