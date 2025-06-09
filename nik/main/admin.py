from django.contrib import admin
from .models import Employee, JobApplication


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'position', 'on_business_trip', 'date')
    list_filter = ('position', 'on_business_trip', 'date')
    search_fields = ('name', 'phone')


@admin.register(JobApplication)
class JobApplicationAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'desired_position', 'status', 'application_date')
    list_filter = ('status', 'application_date')
    search_fields = ('surname', 'name', 'email', 'phone')
    readonly_fields = ('application_date',)