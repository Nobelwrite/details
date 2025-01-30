
from rest_framework import serializers
from .models import MyDetails


class MyDetailsSerializer(serializers.ModelSerializer):
    class Meta:
         models= MyDetails
         fields = ['email', 'github', 'current_datetime']
