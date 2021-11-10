# Generated by Django 3.2.5 on 2021-10-25 10:37

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('enterdata', '0005_auto_20211025_0954'),
    ]

    operations = [
        migrations.AddField(
            model_name='species',
            name='location',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='enterdata.geography'),
            preserve_default=False,
        ),
    ]