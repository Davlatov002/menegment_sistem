from rest_framework import serializers
from apps.group.models.lessons_chedule import LessonsChedule

class LessonsCheduleSerializsr(serializers.ModelSerializer):
    class Meta:
        model = LessonsChedule
        fields = [
            'id',
            'start_time',
            'group',
            'end_time',
            'room_id',
            'deys',
        ]

