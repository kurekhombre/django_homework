from calendar import weekday
from django.shortcuts import render
from datetime import datetime
# Create your views here.
def monday(request):
    today = False
    if datetime.today().weekday() == 0:
        today = True
    else:
        today = False
        
    context = {
        "today": today
    }
    return render(request, "monday/isitmonday.html", context=context)