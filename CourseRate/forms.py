from django import forms
from django.contrib.auth.models import User
from CourseRate.models import UserProfile, University, Departments, Modules, Review


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


class ModuleForm(forms.ModelForm):
    module_name = forms.CharField(max_length=200, help_text="Please enter the name of the module.")

    class Meta:
        model = Modules
        fields = ('module_name',)


class ReviewForm(forms.ModelForm):
    rev_title = forms.CharField(max_length=50, help_text="Enter the title of the review.")
    rev_text = forms.CharField(max_length=750, help_text="Write you review here, max 750 characters.")
    rev_rating = forms.CharField(max_length=30, help_text="Leave your rating here.")
    rev_upvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)
    rev_downvotes = forms.IntegerField(widget=forms.HiddenInput(), initial=0)

    class Meta:
        model = Review
        fields = ('rev_title', 'rev_text', 'rev_rating')
