from rest_framework import serializers

from apps.account.models.staff_profile import StaffProfile

class StaffProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = StaffProfile
        fields = [
            'id',
            'last_name',
            'first_name',
            'user',
            'branch',
            'phone_number',
            'image',
            'salary',
            'position',
            'start_at',
            'end_at',
            'status',
        ]
