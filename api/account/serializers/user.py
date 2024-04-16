from rest_framework import serializers
from apps.account.models.user import User
from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

class CustomTokenObtainPairSerializer(TokenObtainPairSerializer):

    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        token['username'] = user.username
        token['roles'] = user.roles
        token['is_superuser'] = user.is_superuser
        token['id'] = str(user.id)
        return token
    
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = [
            'id',
            'username',
            'password',
            'roles',
            'is_active',
            'is_staff',
            'is_superuser',

        ]

