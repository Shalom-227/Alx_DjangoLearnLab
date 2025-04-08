from rest_framework import serializers
from .models import CustomUser
from django.contrib.auth import authenticate, get_user_model
from rest_framework.authtoken.models import Token

class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField()
    password2 = serializers.CharField(write_only=True)  # Confirm password
    
    class Meta:
        model = CustomUser
        fields = ['username', 'bio', 'profile_picture', 'email', 'password', 'password2']
        extra_kwargs = {'password': {'write_only': True}}

    def validate(self, data):
        """Ensure passwords match"""
        if data['password'] != data['password2']:
            raise serializers.ValidationError({"password": "Passwords do not match."})
        return data

    def create(self, validated_data):
        """Create user with hashed password"""
        validated_data.pop('password2')  # Remove password2 before saving
        user = get_user_model().objects.create_user(**validated_data)  # Hashes password
        Token.objects.create(user=user)
        return user

class LoginSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(required=True)
    password = serializers.CharField(required=True, write_only=True)

    class Meta:
        model = get_user_model()  # Ensure CustomUser model is used
        fields = ["email", "password"]

    def validate(self, data):
        """Authenticate user"""
        email = data.get('email')
        password = data.get('password')

        """Validate user credentials"""
        try:
           user = get_user_model().objects.get(email=email)
        except get_user_model().DoesNotExist:
            raise serializers.ValidationError("Invalid credentials")

        if not user.check_password(password):  # Use check_password to compare the password
            raise serializers.ValidationError("Invalid credentials")

        token, created = Token.objects.get_or_create(user=user)  # Retrieve token or retrieve token if it does not exist
        return {"token": token.key, "user": user}

class TokenSerializer(serializers.ModelSerializer):
    user_id = serializers.IntegerField(source="user.id", read_only=True)
    email = serializers.EmailField(source="user.email", read_only=True)

    class Meta:
        model = Token
        fields = ("key", "user_id", "email")


class UserProfileSerializer(serializers.ModelSerializer):
    followers_count = serializers.SerializerMethodField()
    following_count = serializers.SerializerMethodField()

    class Meta:
        model = CustomUser
        fields = ['username', 'email', 'bio', 'profile_picture', 'followers_count', "following_count"]

    def get_followers_count(self, obj):
        return obj.followers.count()

    def get_following_count(self, obj):
        return obj.following.count()


class FollowSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ['id', 'username']
