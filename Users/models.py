from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

# Create your models here.

class UserManager(BaseUserManager):
	def create_user(self, username, email, age, password=None):
		"""
			Create user with email, age and password
		"""

		if not email:
			raise ValueError('NO email address found!')

		user = self.model(email=self.normalize_email(email), age=age, username=username)
		user.set_password(password)
		user.save(using=self._db)

		return user

	def create_superuser(self, username, email, age, password=None):
		"""
			Create user with email, age and password
		"""

		if not email:
			raise ValueError('NO email address found!')

		user = self.model(email=email, age=age, username=username, password=password)
		user.set_password(password)
		user.is_admin = True
		user.save(using=self._db)


		return user


class User(AbstractBaseUser):
	username = models.CharField(verbose_name='UserName', max_length=255, unique=True)
	email = models.EmailField(verbose_name='Email', max_length=255, unique=True)
	age = models.IntegerField(blank=True)
	is_active = models.BooleanField(default=True)
	is_admin = models.BooleanField(default=False)
	is_staff = models.BooleanField(default=False)

	objects = UserManager()

	def __str__(self) -> str:
		return self.username

	USERNAME_FIELD = 'username'
	REQUIRED_FIELDS = ['email', 'age']

	def has_perm(self, prem, obj=None):
		"Does User Have Specific Permission"
		return True

	def has_module_perms(self, app_label):
		"Does User Have Access to specific App"
		return True

	@property
	def is_staff(self):
		"Is user is Staff"
		return self.is_admin