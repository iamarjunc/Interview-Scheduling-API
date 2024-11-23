from rest_framework import serializers
from .models import User, Availability

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = '__all__'


class UserCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'role']

    def validate_role(self, value):
        if value not in ['candidate', 'interviewer']:
            raise serializers.ValidationError("Role must be 'candidate' or 'interviewer'.")
        return value


class AvailabilitySerializer(serializers.ModelSerializer):
    class Meta:
        model = Availability
        fields = '__all__'
