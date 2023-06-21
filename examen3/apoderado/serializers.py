from rest_framework import serializers
from .models import Apoderado

class ApoderadoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Apoderado
        fields = '__all__'
