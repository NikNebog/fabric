from django.contrib import admin
from .models import Employee, BusinessTripApplication


@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
    list_display = ('name', 'phone', 'position', 'on_business_trip', 'date')
    list_filter = ('position', 'on_business_trip', 'date')
    search_fields = ('name', 'phone')


@admin.register(BusinessTripApplication)
class BusinessTripApplicationAdmin(admin.ModelAdmin):
    list_display = ('surname', 'name', 'position', 'destination', 'start_date', 'end_date', 'status', 'application_date')
    list_filter = ('status', 'destination', 'start_date')
    search_fields = ('surname', 'name', 'destination', 'purpose', 'position')
    date_hierarchy = 'application_date'
    readonly_fields = ('application_date',) # Поле application_date будет только для чтения
    fieldsets = (
        ("Личная информация", {
            'fields': ('surname', 'name', 'patronymic', 'position')
        }),
        ("Информация о командировке", {
            'fields': ('destination', 'purpose', 'funding', 'start_date', 'end_date')
        }),
        ("Статус и примечания", {
            'fields': ('status', 'notes', 'application_date')
        }),
    )