from django import forms
from django.contrib.auth.models import User
from CourseRate.models import UserProfile, University, Departments, Modules


class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text=" ")

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


class UniversityForm(forms.ModelForm):
    university_name = forms.CharField(max_length=200, help_text="Please enter the name of the university.")

    class Meta:
        model = University
        fields = ('university_name',)


class DepartmentForm(forms.ModelForm):
    department_name = forms.CharField(max_length=200, help_text="Please enter the name of the department.")

    class Meta:
        model = Departments
        fields = ('department_name',)
