from django.db import models
from django.contrib.auth.models import User
from django.template.defaultfilters import slugify
from django.utils import timezone


# Stores a user's website and profile picture
class UserProfile(models.Model):
    # This line is required. Links UserProfile to a User model instance.
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # The additional attributes we wish to include.
    website = models.URLField(blank=True)
    picture = models.ImageField(upload_to='profile_images', blank=True)

    def __str__(self):
        return self.user.username


# Represents a university a student may attend
class University(models.Model):
    university_name = models.CharField(max_length=200, unique=True)
    slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.university_name)
        super(University, self).save(*args, **kwargs)

    def __str__(self):
        return self.university_name

    class Meta:
        verbose_name_plural = 'Universities'


# Represents a department a university may have
class Departments(models.Model):
    university = models.ForeignKey(University, on_delete=models.CASCADE)
    department_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    unique_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.department_name)
        self.unique_slug = slugify(self.university.university_name) + "-" + slugify(self.department_name)
        super(Departments, self).save(*args, **kwargs)

    def __str__(self):
        return self.department_name + " | " + self.university.university_name

    class Meta:
        verbose_name_plural = 'Departments'


# Represents a module that a student may take
class Modules(models.Model):
    department = models.ForeignKey(Departments, on_delete=models.CASCADE)
    module_name = models.CharField(max_length=200)
    slug = models.SlugField(unique=False)
    unique_slug = models.SlugField(unique=True)

    def save(self, *args, **kwargs):
        self.slug = slugify(self.module_name)
        self.unique_slug = self.department.unique_slug + "-" + slugify(self.module_name)
        super(Modules, self).save(*args, **kwargs)

    def __str__(self):
        return (self.module_name + " | " + self.department.department_name + " | "
                + self.department.university.university_name)

    class Meta:
        verbose_name_plural = 'Modules'


# Represents a review written by a user
class Review(models.Model):
    module = models.ForeignKey(Modules, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    user_profile = models.ForeignKey(UserProfile, on_delete=models.CASCADE)

    RATING_CHOICES = (("0", "0"), ("1", "1"),
                      ("2", "2"), ("3", "3"),
                      ("4", "4"), ("5", "5"),
                      ("6", "6"), ("7", "7"),
                      ("8", "8"), ("9", "9"),
                      ("10", "10"))

    rev_timestamp = models.DateField(default=timezone.now, blank=True, null=True)
    rev_title = models.CharField(max_length=50)
    rev_text = models.CharField(max_length=750)
    rev_rating = models.CharField(max_length=30, choices=RATING_CHOICES)
    rev_upvotes = models.IntegerField(default=0)
    rev_downvotes = models.IntegerField(default=0)

    def __str__(self):
        return self.module.module_name + '\n' + self.rev_text

    class Meta:
        verbose_name_plural = 'Reviews'
