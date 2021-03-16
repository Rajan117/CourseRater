from django.contrib import admin
from CourseRate.models import UserProfile, University, Departments, Modules


class UniversityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('university_name',)}


admin.site.register(UserProfile)
admin.site.register(University, UniversityAdmin)
admin.site.register(Departments)
admin.site.register(Modules)
