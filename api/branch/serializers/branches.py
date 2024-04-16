from rest_framework import serializers
from apps.branch.models.branches import Branch

class BranchesSerializer(serializers.ModelSerializer):
    class Meta:
        model = Branch
        fields = [
            'id',
            'name', 
            'address',
            'start_at',
            'end_at',
            'status',
        ]