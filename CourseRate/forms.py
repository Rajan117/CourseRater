from django import forms
from django.contrib.auth.models import User
from CourseRate.models import UserProfile, University, Departments, Modules, Review


# A form for creating a user
class UserForm(forms.ModelForm):
    password = forms.CharField(widget=forms.PasswordInput())
    username = forms.CharField(help_text=" ")

    class Meta:
        model = User
        fields = ('username', 'email', 'password',)


# A form for creating a user profile that will be linked to a user
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('website', 'picture',)


# This form creates a university
class UniversityForm(forms.ModelForm):
    university_name = forms.CharField(max_length=200, help_text="Please enter the name of the university.")

    class Meta:
        model = University
        fields = ('university_name',)


# Creates a department
class DepartmentForm(forms.ModelForm):
    department_name = forms.CharField(max_length=200, help_text="Please enter the name of the department.")

    class Meta:
        model = Departments
        fields = ('department_name',)


# Creates a module
class ModuleForm(forms.ModelForm):
    module_name = forms.CharField(max_length=200, help_text="Please enter the name of the course.")

    class Meta:
        model = Modules
        fields = ('module_name',)


# Creates a review from user input
class ReviewForm(forms.ModelForm):
    rev_title = forms.CharField(max_length=50, help_text="Enter the title of the review.")
    rev_text = forms.CharField(max_length=750, help_text="Write your review here, max 750 characters.",
                               widget=forms.Textarea(attrs={'class': "largeTextbox"}))
    rev_rating = forms.CharField(max_length=30, help_text="Rate the course on a scale from 1 to 10.",
                                 widget=forms.TextInput(attrs={'class': "rating"}))
    rev_upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    rev_downvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Review
        fields = ('rev_title', 'rev_text', 'rev_rating')
