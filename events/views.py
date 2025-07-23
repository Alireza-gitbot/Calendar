from django.shortcuts import render
from datetime import date
from .models import Event
from .utils import JalaliCalendar
import jdatetime


def calendar_view(request):
    today = date.today()
    year = today.year
    month = today.month

    cal = JalaliCalendar().formatmonth(year, month)

    # رویدادها + تبدیل تاریخ به شمسی
    events = Event.objects.filter(date__month=month)
    events_list = []

    for event in events:
        jalali_date = jdatetime.date.fromgregorian(date=event.date)
        events_list.append({
            'title': event.title,
            'miladi': event.date,
            'jalali': jalali_date.strftime('%d %B %Y'),
        })

    return render(request, 'events/calender.html', {
        'calendar': cal,
        'events': events_list,
    })

