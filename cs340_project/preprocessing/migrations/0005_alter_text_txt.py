# Generated by Django 3.2 on 2021-04-19 13:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('preprocessing', '0004_auto_20210417_0521'),
    ]

    operations = [
        migrations.AlterField(
            model_name='text',
            name='txt',
            field=models.FileField(help_text='CSV File', upload_to='media/text/', verbose_name='CSV'),
        ),
    ]