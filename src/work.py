import requests
import codecs
from bs4 import BeautifulSoup as BS

headers = {'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/84.0.4147.89 Safari/537.36',
           'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9'
           }

def hh_jobs(url):
#    domain = 'https://www.work.ua'
#    url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=113&clusters=true&enable_snippets=true&items_on_page=100&no_magic=true&search_field=name&search_field=description&specialization=1&text=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE+%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F&page=0'
    resp = requests.get(url, headers=headers)

    jobs = []
    errors = []

    if resp.status_code == 200:
        soup = BS(resp.content, 'html.parser')
        main_div = soup.find('div', attrs={'class' : 'vacancy-serp'})
        if main_div:
            div_list = main_div.find_all('div', attrs={'class' : 'vacancy-serp-item'})
            for div in div_list:
                title = div.find('a', attrs={'class' : 'bloko-link HH-LinkModifier'})
                l = div.find('span', attrs={'class' : 'g-user-content'})
                link = l.a['href']
                content_respon = div.find('div', attrs={'data-qa' : 'vacancy-serp__vacancy_snippet_responsibility'})
                content_requir = div.find('div', attrs={'data-qa' : 'vacancy-serp__vacancy_snippet_requirement'})
                description = content_respon.text + content_requir.text
                company = 'No name'
                logo = div.find('a', attrs={'class' : 'bloko-link bloko-link_secondary'})
                if logo:
                    company = logo.text
                jobs.append({'title': title.text, 'link': link,
                             'description': description, 'company': company})
        else:
            errors.append({'url': link, 'title': "Div does not exists"})
    else:
        errors.append({'url': link, 'title': "Page do not response"})
    return jobs, errors


def work(url):
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

if __name__ == '__main__':
    url = 'https://hh.ru/search/vacancy?L_is_autosearch=false&area=113&clusters=true&enable_snippets=true&items_on_page=100&no_magic=true&search_field=name&search_field=description&specialization=1&text=%D0%A0%D0%B0%D0%B7%D1%80%D0%B0%D0%B1%D0%BE%D1%82%D1%87%D0%B8%D0%BA+%D0%BF%D1%80%D0%BE%D0%B3%D1%80%D0%B0%D0%BC%D0%BC%D0%BD%D0%BE%D0%B3%D0%BE+%D0%BE%D0%B1%D0%B5%D1%81%D0%BF%D0%B5%D1%87%D0%B5%D0%BD%D0%B8%D1%8F&page=0'
    jobs, errors = hh_jobs(url)
    h = codecs.open('work.txt', 'w', 'utf-8')
    h.write(str(jobs))
    h.close()