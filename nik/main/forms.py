from django import forms
from .models import BusinessTripApplication 

class BusinessTripApplicationForm(forms.ModelForm):
    class Meta:
        model = BusinessTripApplication
        fields = [
            'surname', 'name', 'patronymic',
            'position',
            'destination', 'purpose',
            'funding',
            'start_date', 'end_date'
        ]

        widgets = {
            'destination': forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Например: Астана, Казахстан'}),
            'purpose': forms.Textarea(attrs={'rows': 5, 'class': 'form-control', 'placeholder': 'Опишите цель командировки (например, участие в конференции, встреча с клиентами)'}),
            'funding': forms.Textarea(attrs={'rows': 3, 'class': 'form-control', 'placeholder': 'Укажите источник финансирования (например, бюджет компании, грант)'}),
            'start_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
            'end_date': forms.DateInput(attrs={'type': 'date', 'class': 'form-control'}),
        }

        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'position': 'Должность',
            'destination': 'Куда будет командировка',
            'purpose': 'Цель командировки',
            'funding': 'Финансирование',
            'start_date': 'Дата начала командировки',
            'end_date': 'Дата окончания командировки',
        }