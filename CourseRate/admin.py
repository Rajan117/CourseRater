from django.contrib import admin
from CourseRate.models import UserProfile, University, Departments, Modules, Review


class UniversityAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('university_name',)}


class DepartmentsAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('department_name',)}


class ModulesAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('module_name',)}


admin.site.register(UserProfile)
admin.site.register(University, UniversityAdmin)
admin.site.register(Departments, DepartmentsAdmin)
admin.site.register(Modules, ModulesAdmin)
admin.site.register(Review)
