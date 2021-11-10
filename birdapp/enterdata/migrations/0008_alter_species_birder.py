# Generated by Django 3.2.5 on 2021-10-26 21:51

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterdata', '0007_auto_20211026_2150'),
    ]

    operations = [
        migrations.AlterField(
            model_name='species',
            name='birder',
            field=models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]