from django.db import models
from django.conf import settings

class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    position = models.CharField(max_length=100, verbose_name="Должность")
    on_business_trip = models.BooleanField(default=False, verbose_name="В командировке")
    date = models.DateField(auto_now_add=True, verbose_name="Дата")

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"