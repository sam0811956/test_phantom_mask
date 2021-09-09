import os
import re
import json
from sys import path
from django.db import migrations

user_json_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../data/'))
user_filename = 'users.json'


def load_user_data(apps, schema_editor):
    user_file = os.path.join(user_json_dir, user_filename)
    with open(user_file, 'r') as user_data:
        data = json.load(user_data)
        
        User = apps.get_model("mask_api", "User")
        PurchaseHistory = apps.get_model("mask_api", "PurchaseHistory")
        
        for user_data in data:
            us = User(
                        name = user_data['name'],
                        cashbalance = user_data['cashBalance'],
                    )
            us.save()

            for purchase in user_data['purchaseHistories']:
                PurchaseHistory(
                    user = us,
                    pharmacies_name=purchase['pharmacyName'],
                    mask_name=purchase['maskName'],
                    trans_amount=purchase['transactionAmount'],
                    trans_date=purchase['transactionDate'],
                    ).save()

def unload_user_data(apps, schema_editor):
    User = apps.get_model("mask_api", "User")
    PurchaseHistory = apps.get_model("mask_api", "PurchaseHistory")
    for _mod in [User, PurchaseHistory]:
        _mod.objects.all().delete()

class Migration(migrations.Migration):
    dependencies = [
        ('mask_api','0005_auto_20210909_0313'),
    ]

    operations = [
        migrations.RunPython(load_user_data, reverse_code = unload_user_data),
    ]
