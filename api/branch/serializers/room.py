from rest_framework import serializers
from apps.branch.models.room import Room

class RoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = Room
        fields = [
            'id',
            'name',
            'number',
            'max_count',
            'branch',
        ]