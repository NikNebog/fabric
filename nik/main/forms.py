from django import forms
from .models import JobApplication

class JobApplicationForm(forms.ModelForm):
    class Meta:
        model = JobApplication
        fields = [
            'surname', 'name', 'patronymic',
            'phone', 'email',
            'desired_position', 'desired_salary',
            'experience', 'education', 'skills',
            'cover_letter', 'resume'
        ]
        
        widgets = {
            'cover_letter': forms.Textarea(attrs={'rows': 5, 'class': 'form-control'}),
            'experience': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'education': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'skills': forms.Textarea(attrs={'rows': 3, 'class': 'form-control'}),
            'phone': forms.TextInput(attrs={'placeholder': '+7 (XXX) XXX-XX-XX'}),
        }
        
        labels = {
            'surname': 'Фамилия',
            'name': 'Имя',
            'patronymic': 'Отчество',
            'phone': 'Телефон',
            'email': 'Электронная почта',
            'desired_position': 'Желаемая должность',
            'desired_salary': 'Желаемая зарплата',
            'experience': 'Опыт работы',
            'education': 'Образование',
            'skills': 'Профессиональные навыки',
            'cover_letter': 'Сопроводительное письмо',
            'resume': 'Резюме (PDF или DOCX)',
        }