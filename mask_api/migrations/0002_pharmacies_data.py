import os
import re
import json
from sys import path
from django.db import migrations

pharmacies_json_dir = os.path.abspath(
        os.path.join(os.path.dirname(__file__), '../../data/'))
pharmacies_filename = 'pharmacies.json'


def parse_op_hour(op_h_str):
    op_hour_data=[]

    for time_item in op_h_str.split('/'):
        week_days_datas = re.findall(
            "(Mon|Tue|Wed|Thu|Fri|Sat|Sun)+", time_item)
        hour_datas = re.findall("(\d+):(\d+)", time_item)
        hour_min_datas = set_hours_mins_data(hour_datas)

        for week_day in week_days_datas:
            hour_min_dict_data = hour_min_datas.copy()
            hour_min_dict_data['week_day'] = week_day
            op_hour_data += [hour_min_dict_data]

    return op_hour_data
           


def set_hours_mins_data(hour_datas):
    #[('12', '56'),('21','58')]
    start_data, end_data = hour_datas
    start_hour, start_min = start_data
    end_hour, end_min = end_data
    return {
        'start_hour': start_hour,
        'start_min': start_min,
        'end_hour': end_hour,
        'end_min': end_min
    }
            

def load_pharmacies(apps, schema_editor):
    pharmacies_file = os.path.join(pharmacies_json_dir, pharmacies_filename)
    
    with open(pharmacies_file, 'r') as pharmacies:
        data = json.load(pharmacies)

        PharMacies = apps.get_model("mask_api", "PharMacies")
        Mask = apps.get_model("mask_api", "Mask")
        OpeningHour = apps.get_model("mask_api", "OpeningHour")

        for pharm_data in data:
            phar = PharMacies(
                    name = pharm_data['name'],
                    cashbalance=pharm_data['cashBalance'],
                    )
            phar.save()
            
            for mask_data in pharm_data['masks']:
                Mask(
                        pharmacies=phar,
                        name=mask_data['name'],
                        price=mask_data['price'],
                        ).save()

            for open_hours in parse_op_hour(pharm_data['openingHours']):
                OpeningHour(
                    pharmacies=phar,
                    week_day=open_hours['week_day'],
                    start_hour=open_hours['start_hour'],
                    start_min=open_hours['start_min'],
                    end_hour=open_hours['end_hour'],
                    end_min=open_hours['end_min'],
                    ).save()

        
def unload_pharmacies(apps, schema_editor):
    PharMacies = apps.get_model("mask_api", "PharMacies")
    Mask = apps.get_model("mask_api", "Mask")
    OpeningHour = apps.get_model("mask_api", "OpeningHour")
    for _model in [PharMacies, Mask, OpeningHour]:
        _model.objects.all().delete()
    

class Migration(migrations.Migration):
    dependencies = [
        ('mask_api', '0001_initial'),
        ]

    operations = [
        migrations.RunPython(load_pharmacies, unload_pharmacies),
        ]
