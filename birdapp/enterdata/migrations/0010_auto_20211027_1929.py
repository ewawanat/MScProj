# Generated by Django 3.2.5 on 2021-10-27 19:29

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('enterdata', '0009_remove_species_birder'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='species',
            name='date_seen',
        ),
        migrations.RemoveField(
            model_name='species',
            name='location',
        ),
        migrations.RemoveField(
            model_name='species',
            name='photo',
        ),
        migrations.CreateModel(
            name='Sighting',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date_seen', models.DateField(blank=True)),
                ('photo', models.ImageField(blank=True, default='default.png', upload_to='')),
                ('birder', models.ForeignKey(blank=True, default=None, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='enterdata.geography')),
                ('species_name', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, to='enterdata.species')),
            ],
        ),
    ]