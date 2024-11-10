from rest_framework import serializers
from .models import Profile


class UpdateVerifyCodeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['phone', 'email', 'verify_code']


class ProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = Profile
        fields = ['homelessAnimals', 'pets', 'volunteer', 'shelterWorker', 'petOwner']

class RegisterSerializer(serializers.ModelSerializer):
    phone = serializers.CharField(max_length=20)
    photo = serializers.ImageField(required=False, allow_null=True)

    class Meta:
        model = Profile
        fields = ['name', 'phone', 'photo']


class SMSVerificationSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
    code = serializers.CharField(max_length=6)


class LoginSerializer(serializers.Serializer):
    phone_number = serializers.CharField(max_length=15)
