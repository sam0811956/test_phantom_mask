# Generated by Django 3.2.7 on 2021-09-09 02:43

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('mask_api', '0002_pharmacies_data'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('cashbalance', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='PurchaseHistory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('pharmacies_name', models.CharField(max_length=100)),
                ('mask_name', models.CharField(max_length=100)),
                ('trans_amount', models.FloatField()),
                ('trans_date', models.DateTimeField(blank=True, null=True)),
                ('pharmacies', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='purchasehistory', to='mask_api.pharmacies')),
            ],
        ),
    ]
