from django import forms
from footBallApp.models import UserProfileInfo, Teams, TeamMembers, MatchScheduling
from django.contrib.auth.models import User


class UserForm(forms.ModelForm):
	"""
	Form design for storing authentication informations to default user model
	"""
	password = forms.CharField(widget=forms.PasswordInput())
	class Meta():
		model = User
		fields = ('username','password','email')


class UserProfileInfoForm(forms.ModelForm):
	"""
	Form design for extending the default user model 
	"""
	class Meta():
		model = UserProfileInfo
		fields = ('name','age', 'user_type')

class TeamForm(forms.ModelForm):
	"""
	Form design for creating a team 
	"""
	class Meta():
		model = Teams
		exclude = ()

class TeamMemberForm(forms.ModelForm):
	"""
	Form design for creating a team member
	"""
	class Meta():
		model = TeamMembers
		exclude = ()

class MatchSchedulingForm(forms.ModelForm):
	"""
	Form design for scheduling matches
	"""
	class Meta():
		model = MatchScheduling
		exclude = ()