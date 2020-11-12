from django.contrib.auth import get_user_model, authenticate
from django.http import request
#When we output text to screen auto translates to the correct language
from django.utils.translation import ugettext_lazy as _
from rest_framework import serializers

class UserSerializer(serializers.ModelSerializer):
    """Serializer for the users object"""

    class Meta:
        model = get_user_model()
        fields = ('email', 'password', 'name')
        # Configure some extra settings in the serializer
        extra_kwargs = {'password': {'write_only': True, 'min_length': 5}}

    # Called when we create a new object
    def create(self, validated_data):
        """Create a new user with encrypted password and return it"""
        return get_user_model().objects.create_user(**validated_data)

class AuthTokenSerializer(serializers.Serializer):
    """Serializer for the user authentication object"""
    email = serializers.CharField()
    password = serializers.CharField(
        style={'input_type': 'password'},
        trim_whitespace=False
    )

    #Validation checks that the types are correct

    def validate(self, attrs):
        """Validate and authenticate the user"""
        email = attrs.get('email')
        password = attrs.get('password')

        #Gets the request from the the view
        user = authenticate(
            request=self.context.get('request'),
            username=email,
            password=password
        )
        if not user:
            message = _('Unable to authenticate with provided credentials')
            #Automatically django raises 400 response by using ValidationError 
            raise serializers.ValidationError(message, code='authentication')

        #We need to do that always...
        attrs['user'] = user
        return attrs