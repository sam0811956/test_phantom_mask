# Generated by Django 3.2.7 on 2021-09-08 08:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PharMacies',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cashbalance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='OpeningHour',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('week_day', models.CharField(choices=[('Mon', 'Monday'), ('Tues', 'Tuesday'), ('Wed', 'Wednesday'), ('Thurs', 'Thursday'), ('Fri', 'Friday'), ('Sat', 'Saturday'), ('Sun', 'Sunday')], max_length=5)),
                ('start_hour', models.PositiveSmallIntegerField(null=True)),
                ('start_min', models.PositiveSmallIntegerField(null=True)),
                ('end_hour', models.PositiveSmallIntegerField(null=True)),
                ('end_min', models.PositiveSmallIntegerField(null=True)),
                ('pharmacies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask_api.pharmacies')),
            ],
        ),
        migrations.CreateModel(
            name='Mask',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('price', models.FloatField()),
                ('pharmacies', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='mask_api.pharmacies')),
            ],
        ),
    ]
