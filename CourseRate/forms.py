from django import forms
from django.contrib.auth.models import User
from CourseRate.models import UserProfile, University, Departments, Modules


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class UniversityForm(forms.ModelForm):
    name = forms.CharField(max_length=200, help_text="Please enter the name of the university.")
    slug = forms.CharField(widget=forms.HiddenInput(), required=False)

    class Meta:
        model = University
        fields = ('university_name',)
