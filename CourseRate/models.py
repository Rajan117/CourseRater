from django.db import models
from django.contrib.auth.models import User


class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


class University(models.Model):

    university_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name_plural = 'Universities'


class Departments(models.Model):

    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200, unique=True)


    def __str__(self):
        return self.department_name + " | " + self.university.university_name

    class Meta:
        verbose_name_plural = 'Departments'

class Modules(models.Model):

    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=200, unique=True)

    def __str__(self):
        return (self.module_name + " | " + self.department.department_name + " | "
                + self.department.university.university_name)

    class Meta:
        verbose_name_plural = 'Modules'
