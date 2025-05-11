from rest_framework import serializers
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken

# Register serializer
from rest_framework import serializers
from .models import User

from rest_framework import serializers
from django.contrib.auth import authenticate
from .models import User  # Assuming your custom user model is called User

# User Registration Serializer
class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)
    role = serializers.ChoiceField(choices=User.ROLE_CHOICES, default=User.USER)  # Add role field

    class Meta:
        model = User
        fields = ['username', 'password', 'role']  # Include role in the fields

    def create(self, validated_data):
        password = validated_data.pop('password')
        user = User.objects.create(**validated_data)
        user.set_password(password)  # Hash the password
        user.save()
        return user


# Login Serializer
class LoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True)

    def validate(self, data):
        username = data.get('username')
        password = data.get('password')

        # Authenticate the user
        user = authenticate(username=username, password=password)
        
        if not user:
            raise serializers.ValidationError("Invalid username or password")

        return {
            'user': user
        }

# Token serializer for JWT
class TokenSerializer(serializers.ModelSerializer):
    class Meta:
        model = get_user_model()
        fields = ['username']

    def create_token(self, user):
        refresh = RefreshToken.for_user(user)
        return {
            'access_token': str(refresh.access_token),
            'refresh_token': str(refresh),
        }
