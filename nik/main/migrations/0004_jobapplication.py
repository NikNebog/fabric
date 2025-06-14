# Generated by Django 5.2.1 on 2025-06-09 06:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main', '0003_employee_business_trip_city_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='JobApplication',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100, verbose_name='Имя')),
                ('surname', models.CharField(max_length=100, verbose_name='Фамилия')),
                ('patronymic', models.CharField(blank=True, max_length=100, verbose_name='Отчество')),
                ('phone', models.CharField(max_length=20, verbose_name='Номер телефона')),
                ('email', models.EmailField(max_length=254, verbose_name='Электронная почта')),
                ('desired_position', models.CharField(max_length=100, verbose_name='Желаемая должность')),
                ('desired_salary', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True, verbose_name='Желаемая зарплата')),
                ('application_date', models.DateTimeField(auto_now_add=True, verbose_name='Дата подачи заявки')),
                ('status', models.CharField(choices=[('pending', 'На рассмотрении'), ('interview', 'Приглашен на собеседование'), ('rejected', 'Отклонена'), ('accepted', 'Принята')], default='pending', max_length=20, verbose_name='Статус заявки')),
                ('experience', models.TextField(blank=True, verbose_name='Опыт работы')),
                ('education', models.TextField(blank=True, verbose_name='Образование')),
                ('skills', models.TextField(blank=True, verbose_name='Навыки')),
                ('cover_letter', models.TextField(blank=True, verbose_name='Сопроводительное письмо')),
                ('resume', models.FileField(blank=True, null=True, upload_to='resumes/', verbose_name='Резюме')),
                ('notes', models.TextField(blank=True, verbose_name='Примечания')),
            ],
            options={
                'verbose_name': 'Заявка на работу',
                'verbose_name_plural': 'Заявки на работу',
                'ordering': ['-application_date'],
            },
        ),
    ]
