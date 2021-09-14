from rest_framework import serializers
from mask_api.models import PharMacies, Mask, OpeningHour, User, PurchaseHistory

class PharMacies_Serializer(serializers.ModelSerializer):
    class Meta:
        model = PharMacies
        fields = ['name', 'cashbalance']

class Mask_Serializer(serializers.ModelSerializer):
    class Meta:
        model = Mask
        fields = ['pharmacies','name', 'price']

class OpeningHour_Serializer(serializers.ModelSerializer):
    class Meta:
        model = OpeningHour
        fields = ['week_day', 'start_hour', 'start_min', 'end_hour', 'end_min']


        
