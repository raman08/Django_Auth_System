from djoser.serializers import UserCreateSerializer, UserSerializer

from rest_framework import serializers

from .models import User

class UserCreateSerializer(UserCreateSerializer):
	class Meta(UserCreateSerializer.Meta):
		model = User
		fields = (
			'id',
			'email',
			'username',
			'password',
			'first_name',
			'last_name',
			'get_full_name',
			'bio',
			'profile_pic',
			'github_profile')

class UserSerializer(UserSerializer):
	class Meta(UserSerializer.Meta):
		model = User
		fields = (
			'id',
			'email',
			'username',
			'password',
			'get_full_name',
			'bio',
			'profile_pic',
			'github_profile')