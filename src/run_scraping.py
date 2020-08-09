import codecs
import os, sys

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ['DJANGO_SETTINGS_MODULE'] = 'pj_scraping_service.settings'

import django
django.setup()


from scraping.work import *
from scraping.models import City, Language, Jobs_list


parsers = (
    (hh_jobs, 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=113&clusters=true&enable_snippets=true&items_on_page=100&no_magic=true&search_field=name&search_field=description&specialization=1&text=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE+%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F&page=0'),
    (work, 'https://www.work.ua/ru/jobs-kiev-python/'),
)

city = City.objects.filter(slug='moskva')
print(city)

jobs, errors = [], []
for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e


h = codecs.open('work.txt', 'w', 'utf-8')
h.write(str(jobs))
h.close()