from django.db import models
from django.conf import settings

class Employee(models.Model):
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия", blank=True)
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    work_email = models.EmailField(verbose_name="Рабочая почта", blank=True)

    position = models.CharField(max_length=100, verbose_name="Должность")
    
    on_business_trip = models.BooleanField(default=False, verbose_name="В командировке")
    business_trip_start = models.DateField(null=True, blank=True, verbose_name="Начало командировки")
    business_trip_end = models.DateField(null=True, blank=True, verbose_name="Окончание командировки")
    business_trip_region = models.CharField(max_length=100, blank=True, verbose_name="Регион командировки")
    business_trip_city = models.CharField(max_length=100, blank=True, verbose_name="Город командировки")
    business_trip_task = models.TextField(blank=True, verbose_name="Задание на командировку")

    date = models.DateField(auto_now_add=True, verbose_name="Дата добавления")

    def __str__(self):
        return f"{self.surname} {self.name}"

    class Meta:
        verbose_name = "Сотрудник"
        verbose_name_plural = "Сотрудники"


class BusinessTripApplication(models.Model):

    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    name = models.CharField(max_length=100, verbose_name="Имя")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", blank=True)

    position = models.CharField(max_length=100, verbose_name="Должность")

    destination = models.CharField(max_length=255, verbose_name="Куда будет командировка")
    purpose = models.TextField(verbose_name="Цель командировки")
    funding = models.TextField(verbose_name="Финансирование", blank=True)

    start_date = models.DateField(verbose_name="Дата начала командировки")
    end_date = models.DateField(verbose_name="Дата окончания командировки")


    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'На рассмотрении'),
            ('approved', 'Одобрена'),
            ('rejected', 'Отклонена'),
            ('completed', 'Завершена'),
        ],
        default='pending',
        verbose_name="Статус заявки"
    )

    application_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи заявки")

    notes = models.TextField(verbose_name="Примечания", blank=True)

    def __str__(self):
        return f"Заявка на командировку от {self.surname} {self.name} в {self.destination}"

    class Meta:
        verbose_name = "Заявка на командировку"
        verbose_name_plural = "Заявки на командировку"
        ordering = ['-application_date']