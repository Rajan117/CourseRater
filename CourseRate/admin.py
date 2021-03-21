from django.contrib import admin
from CourseRate.models import UserProfile, University, Departments, Modules, Review


class UniversityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('university_name',)}


class DepartmentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('department_name',)}


admin.site.register(UserProfile)
admin.site.register(University, UniversityAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Modules)
admin.site.register(Review)
