import calendar
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from .models import Employee

def index_view(request):
    return render(request, 'index/index.html', {
        'now': datetime.now()
    })

def logged_out_view(request):
    return render(request, 'index/registration/logged_out.html')


@login_required
def profile_view(request):
    user = request.user
    try:
        employee = Employee.objects.get(name=user.username)
    except Employee.DoesNotExist:
        employee = None

    return render(request, 'index/profile.html', {'user': user, 'employee': employee})

@login_required
def info_view(request):
    user = request.user
    try:
        employee = Employee.objects.get(name=user.username)
    except Employee.DoesNotExist:
        employee = None

    return render(request, 'index/info.html', {'user': user, 'employee': employee})


def calendar_view(request):
    now = datetime.now()
    year = now.year
    month = now.month

    cal = calendar.HTMLCalendar().formatmonth(year, month)
    
    context = {
        'calendar': cal,
        'month': now.strftime('%B'),
        'year': year,
    }
    return render(request, 'index/index.html', context)


