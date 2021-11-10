# Generated by Django 3.2.5 on 2021-10-22 21:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('enterdata', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='photo',
            field=models.ImageField(blank=True, default='default.png', upload_to=''),
        ),
        migrations.AlterField(
            model_name='species',
            name='date_seen',
            field=models.DateTimeField(),
        ),
    ]