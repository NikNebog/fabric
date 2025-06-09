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


class JobApplication(models.Model):
    # Личная информация
    name = models.CharField(max_length=100, verbose_name="Имя")
    surname = models.CharField(max_length=100, verbose_name="Фамилия")
    patronymic = models.CharField(max_length=100, verbose_name="Отчество", blank=True)
    
    # Контактная информация
    phone = models.CharField(max_length=20, verbose_name="Номер телефона")
    email = models.EmailField(verbose_name="Электронная почта")
    
    # Информация о позиции
    desired_position = models.CharField(max_length=100, verbose_name="Желаемая должность")
    desired_salary = models.DecimalField(
        max_digits=10, 
        decimal_places=2, 
        verbose_name="Желаемая зарплата",
        null=True, 
        blank=True
    )
    
    # Информация о заявке
    application_date = models.DateTimeField(auto_now_add=True, verbose_name="Дата подачи заявки")
    status = models.CharField(
        max_length=20,
        choices=[
            ('pending', 'На рассмотрении'),
            ('interview', 'Приглашен на собеседование'),
            ('rejected', 'Отклонена'),
            ('accepted', 'Принята'),
        ],
        default='pending',
        verbose_name="Статус заявки"
    )
    
    # Дополнительная информация
    experience = models.TextField(verbose_name="Опыт работы", blank=True)
    education = models.TextField(verbose_name="Образование", blank=True)
    skills = models.TextField(verbose_name="Навыки", blank=True)
    cover_letter = models.TextField(verbose_name="Сопроводительное письмо", blank=True)
    
    # Ссылка на резюме (если загружается файл)
    resume = models.FileField(
        upload_to='resumes/',
        verbose_name="Резюме",
        null=True,
        blank=True
    )
    
    notes = models.TextField(verbose_name="Примечания", blank=True)

    def __str__(self):
        return f"Заявка от {self.surname} {self.name} на позицию {self.desired_position}"

    class Meta:
        verbose_name = "Заявка на работу"
        verbose_name_plural = "Заявки на работу"
        ordering = ['-application_date']