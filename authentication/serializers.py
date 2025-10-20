from rest_framework import serializers
from django.contrib.auth import get_user_model
from authentication.models import User  # Adjust the import based on your actual model location

User = get_user_model()

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['id', 'username', 'email', 'first_name', 'last_name', 'role', 'course', 'semester']

