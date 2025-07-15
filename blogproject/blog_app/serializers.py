from rest_framework import serializers
from django.contrib.auth.password_validation import validate_password
from .models import CustomUser, BlogPost


class RegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        write_only=True,
        required=True,
        validators=[validate_password]
    )

    class Meta:
        model = CustomUser
        fields = ('username', 'email', 'mobile_number', 'password', 'role')

    # Override the default create method 
    def create(self, validated_data):
        user = CustomUser.objects.create_user(
            username=validated_data['username'],
            email=validated_data['email'],
            mobile_number=validated_data['mobile_number'],
            password=validated_data['password'],
            role=validated_data['role']
        )
        return user

#Serializer for BlogPost model
class BlogPostSerializer(serializers.ModelSerializer):
    class Meta:
        model = BlogPost
        fields = '__all__'
        # These fields should not be editable by the user
        read_only_fields = ['author', 'publication_date']
