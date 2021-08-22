from django.contrib import admin
from django import forms
from django.contrib.auth.models import Group
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.forms import ReadOnlyPasswordHashField
from django.core.exceptions import ValidationError
from django.db import models
from django.db.models import fields

from Users.models import User

# Register your models here.

class UserCreationForm(forms.ModelForm):
	"""
		A from for createing the new Users.
		Expect Password and Repeat Password
	"""

	password1 = forms.CharField(label='Password', widget=forms.PasswordInput)
	password2 = forms.CharField(label='Repeat Password', widget=forms.PasswordInput)
	print(password1, password2)

	class Meta:
		model = User
		fields = ('email', 'username', 'age')

	def clean_password2(self):
		password1 = self.cleaned_data.get('password1')
		password2 = self.cleaned_data.get('password2')

		print(password1, password2)


		if password1 and password2 and password1 != password2:
			raise ValidationError('Password must be same')

		return password2

	def save(self, commit=True):
		user = super().save(commit=False)
		user.set_password(self.cleaned_data['password1'])

		if commit:
			user.save()

		return user


class UserChangeForm(forms.ModelForm):
	password=ReadOnlyPasswordHashField()

	class Meta:
		model = User
		fields = ['username', 'email', 'password', 'age', 'is_active', 'is_admin', ]
	pass

class UserAdmin(BaseUserAdmin):
	pass

	form = UserChangeForm
	add_form = UserCreationForm

	# List of Displayed Fields
	list_display = ('username', 'email', 'is_admin')
	list_filter = ('is_admin', 'age')

	fieldsets = (
		(None, {'fields': ('username', 'password')}),
		('Personal Info', {'fields': ('email', 'age')}),
		('Permissions', {'fields': ('is_admin', )}),
	)

	# The fields for adding user
	add_fieldsets = (
		(None, {
			'classes' : ('wide',),
			'fields' : ('username', 'email', 'age', 'password1', 'password2',)
		}),
	)

	search_fields = ('email', 'username',)
	ordering = ('username', )
	filter_horizontal = ()

# Registering the new UserAdmin
admin.site.register(User, UserAdmin)

admin.site.unregister(Group)