import calendar
from datetime import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .models import Employee
from .forms import JobApplicationForm
import json


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

@login_required
def trip_view(request):
    user = request.user
    try:
        employee = Employee.objects.get(name=user.username)
    except Employee.DoesNotExist:
        employee = None

    return render(request, 'index/trip.html', {'user': user, 'employee': employee})


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


def dashboard_view(request):
    trips = Employee.objects.all().values('business_trip_start', 'business_trip_end')
    trip_data = [
        {
            'start': trip['business_trip_start'].isoformat(),
            'end': trip['business_trip_end'].isoformat()
        }
        for trip in trips
    ]
    return render(request, 'index/index.html', {'trip_data': json.dumps(trip_data)})



def job_application_view(request):
    if request.method == 'POST':
        form = JobApplicationForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('job_application')  # Перенаправление после успешной отправки
    else:
        form = JobApplicationForm()
    return render(request, 'index/job_application_form.html', {'form': form})




