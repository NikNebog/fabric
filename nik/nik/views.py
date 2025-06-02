import calendar
from datetime import datetime
from django.shortcuts import render
from django.contrib.auth.decorators import login_required

def index_view(request):
    return render(request, 'main/index/index.html') 

def logged_out_view(request):
    return render(request, 'main/index/registration/logged_out.html')

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
    return render(request, 'main/index/index.html', context)


