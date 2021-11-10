# Generated by Django 3.2.5 on 2021-10-23 12:16

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='DisplayForm',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('species_name', models.CharField(max_length=30)),
                ('location', models.CharField(max_length=50)),
                ('from_date', models.DateTimeField()),
                ('to_date', models.DateTimeField()),
            ],
        ),
    ]