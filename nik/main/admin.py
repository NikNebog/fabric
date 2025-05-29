from django.contrib import admin
from .models import Employee

@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'position', 'on_business_trip', 'date')
    list_filter = ('position', 'on_business_trip', 'date')
    search_fields = ('name', 'phone')