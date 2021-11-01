from rest_framework import serializers
from django.contrib.auth.models import User
from EnvergaDB.models import Records


# Record Serializer
class RecordSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Records
        fields = ('id', 'author', 'description', 'date_modified',
                  'date_created', 'status')


# User Serializer
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email')


# Register Serializer
class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 'email', 'password')
        extra_kwargs = {'password': {'write_only': True}}

    def create(self, validated_data):
        user = User.objects.create_user(
            validated_data['username'],
            validated_data['email'],
            validated_data['password']
        )
        return user
