from rest_framework import serializers
from apps.account.models.student_profile import StudentProfile

class StudentProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StudentProfile
        fields = [
            'id',
            'last_name',
            'first_name',
            'user',
            'phone_number1',
            'phone_number2',
            'image',
            'start_at',
            'end_at',
            'status',
        ]


