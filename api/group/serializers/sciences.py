from rest_framework import serializers
from apps.group.models.sciences import Scienc

class SciencesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Scienc
        fields = [
            'id',
            'price',
            'name',
            'start_at',
            'end_at',
            'status',
        ]