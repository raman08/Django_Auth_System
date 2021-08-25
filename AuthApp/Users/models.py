from django.db import models
from django.contrib.auth.models import AbstractUser

import os

# Create your models here.
class User(AbstractUser):
	"""
		Custom User Manager
	"""

	def custom_profile_pic_name(instance, filename):
		print(instance, filename)
		username = instance.get_full_name().replace(" ", "_")
		return f'users/profile/{username}/{filename}'

	username = models.CharField(verbose_name='UserName', max_length=255, unique=True)
	email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
	age = models.IntegerField(blank=True, null=True)
	bio = models.TextField()
	profile_pic = models.ImageField(blank=True, null=True, upload_to=custom_profile_pic_name, verbose_name='Profile')
	github_profile = models.URLField(verbose_name='Github Profile', null=True, blank=True)


	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'first_name', 'last_name', 'bio', 'github_profile', 'profile_pic']

	def get_full_name(self) -> str:
		return f'{self.first_name} {self.last_name}'

	def __str__(self) -> str:
		return self.username
