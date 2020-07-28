import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
           }

domain = 'https://www.work.ua'
url = 'https://www.work.ua/ru/jobs-kiev-python/'
resp = requests.get(url, headers=headers)

jobs = []
errors = []

if resp.status_code == 200:
    soup = BS(resp.content, 'html.parser')
    main_div = soup.find('div', id='pjax-job-list')
    if main_div:
        div_list = main_div.find_all('div', attrs={'class' : 'job-link'})
        for div in div_list:
            title = div.find('h2')
            link = title.a['href']
            content = div.p.text
            company = 'No name'
            logo = div.find('img')
            if logo:
                company = logo['alt']
            jobs.append({'title' : title.text, 'link' : domain + link,
                         'description' : content, 'company' : company})
    else:
        errors.append({'url': link, 'title': "Div does not exists"})
else:
    errors.append({'url' : link, 'title' : "Page do not response"})

#status_debug = 0

h = codecs.open('work.txt', 'w', 'utf-8')
#h = open('work.html', 'w')
h.write(str(jobs))
h.close()