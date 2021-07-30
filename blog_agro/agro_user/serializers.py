from django.contrib.auth.password_validation import validate_password
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator

from agro_user.models import AgroUser


class AgroUserSerializer(serializers.ModelSerializer):
    model = AgroUser
    fields = ('id',
              'username',
              'first_name',
              'last_name',
              'email',
              'password',
              'password2')


class UserDuplicateSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroUser
        fields = ('username', 'first_name', 'last_name')


class RegisterSerializer(serializers.ModelSerializer):
    email = serializers.EmailField(
        required=True,
        validators=[UniqueValidator(queryset=AgroUser.objects.all())]
    )

    password = serializers.CharField(write_only=True,
                                     required=True, validators=[validate_password])

    password2 = serializers.CharField(write_only=True, required=True)

    class Meta:
        model = AgroUser
        fields = ('username', 'password', 'password2', 'email')
        extra_kwargs = {
            'first_name': {'required': False},
            'last_name': {'required': False}
        }

    def validate(self, attrs):
        if attrs['password'] != attrs['password2']:
            raise serializers.ValidationError(
                {'password': 'Password fields did not match'})
        return attrs

    def validate_username(self, value):
        data = self.get_initial()
        username = data.get('username')
        username_qs = AgroUser.objects.filter(username=username)
        if username_qs.exists():
            duplicate_obj = AgroUser.objects.get(username=username)
            serializer = UserDuplicateSerializer(duplicate_obj)
            raise ValidationError('This username has been registered!' + str(serializer.data))
        else:
            pass
        return value

    def create(self, validated_data):
        user = AgroUser(username=validated_data['username'],
                        email=validated_data['email'],
                        is_client=True)
        user.set_password(validated_data['password'])
        user.save()
        return user


class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(min_length=2, max_length=20, required=True)
    email = serializers.EmailField(required=True)
    password = serializers.CharField(min_length=8, max_length=20, required=True, write_only=True)



class AgroUserSearchSerializer(serializers.ModelSerializer):
    class Meta:
        model = AgroUser
        fields = ('id', 'username',)