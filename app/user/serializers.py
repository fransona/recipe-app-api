"""
Serializers for the user API view
"""

from django.contrib.auth import (
    get_user_model,
    authenticate,  # authenticate with django authenticate system
)
from rest_framework import serializers
from django.utils.translation import gettext_lazy as _


class UserSerializer(serializers.ModelSerializer):
    """Serializer for the user object."""

    class Meta:
        # Telling the serializer which model we have to use
        model = get_user_model()
        # Fields that can be changed through API
        fields = ['email', 'password', 'name']
        extra_kwargs = {'password':  {'write_only': True, 'min_length': 5}}

    def create(self, validated_data):
        """Create and return a user with encrypted password"""
        return get_user_model().objects.create_user(**validated_data)


class AuthTokenSerializer(serializers.Serializer):
    """Serializer of the user auth token"""
    email = serializers.EmailField()
    password = serializers.CharField(
        # hide th password while typing in browser
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password,
        )
        if not user:
            msg = _('Unable to authenticate with the porovided credentials')
            raise serializers.ValidationError(msg, code='authorization')

        attrs['user'] = user
        return attrs
