from django.shortcuts import render
from .models import Jobs_list
from .forms import FindForm

# Create your views here.

def home_view(request):
    city = request.GET.get('city')
    language = request.GET.get('language')
    form = FindForm()
    return render(request, 'scraping/home.html', {'object_list' : data_acquisition(city, language), 'form' : form})

def data_acquisition(city, language):
    qs = []
    if city or language:
        _filter = {}
        if city:
            _filter['city__id'] = city
        if language:
            _filter['language__id'] = language
        qs = Jobs_list.objects.filter(**_filter)
    else:
        qs = Jobs_list.objects.all()
    return qs