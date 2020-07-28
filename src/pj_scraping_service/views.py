import django.shortcuts
import datetime


def home(request):
    date = datetime.datetime.now().date()
    name = 'Dmitry'
    _context = {'date': date, 'name': name}
    return django.shortcuts.render(request, 'home.html', _context)

