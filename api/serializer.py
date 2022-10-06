from dataclasses import fields
from rest_framework import serializers
from wallet.models import Customer

class CustomerSerializer(serializers.moduleSerializer):
    class meta:
        model =Customer
        fields= ("first_name","email","age")