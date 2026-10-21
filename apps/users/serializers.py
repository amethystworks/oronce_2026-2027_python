from rest_framework import serializers 
from django.contrib.auth.password_validation import validate_password
from .models import User

class CreateUserSerializer (serializers.ModelSerializer):
    confirm_password = serializers.CharField(write_only=True)
    
    class Meta:
        model = User 
        fields = ['id', 
                  'username', 
                  'email', 
                  'first_name', 
                  'last_name', 
                  'password', 
                  'confirm_password', 
                  'avatar', 
                  'level']
        extra_kwargs = {'password': {'write_only': True}}
        
    def validate(self, attrs):
        password = attrs.get("password", None)
        
        confirm_password = attrs.pop("confirm_password")
        if password != confirm_password:
            raise serializers.ValidationError("Password is not match")
        
        self.is_valid()
        self.save()
        return super().validate(attrs)
    
    def update(self, instance, validated_data):
        return super().update(instance, validated_data)
    