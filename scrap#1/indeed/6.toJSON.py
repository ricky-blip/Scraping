# 1,2.import library JSON, os
import os
import json
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

site = 'https://www.indeed.com'
params = {
    'q': 'Python Developer',
    'l': 'New York State',
    '_ga': '2.211888532.1245593939.1644811576-189846848.1644239158',
    'vjk': 'e401694644bd6752'
}

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
}

res = requests.get(url, params=params, headers=headers)


def get_totalpages():
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        '_ga': '2.251096133.2122936263.1644239158-189846848.1644239158',
        'vjk': 'e401694644bd6752'
    }

    res = requests.get(url, params=params, headers=headers)

    try:
        os.mkdir('temp')
    except FileExistsError:
        pass

    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()

    total_pages = []
    soup = BeautifulSoup(res.text, 'html.parser')

    pagination = soup.find('ul', 'pagination-list')
    pages = pagination.find_all('li')

    for page in pages:

        total_pages.append(page.text)

    total = int(max(total_pages))
    return total


def get_all_items():
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        '_ga': '2.211888532.1245593939.1644811576-189846848.1644239158',
        'vjk': 'e401694644bd6752'
    }
    res = requests.get(url, params=params, headers=headers)
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
    soup = BeautifulSoup(res.text, 'html.parser')

    contents = soup.find_all('table', 'jobCard_mainContent big6_visualChanges')

    job_list = []

    for item in contents:
        title = item.find('h2', 'jobTitle').text
        company = item.find('span', 'companyName')
        company_name = company.text
        try:
            company_link = site + company.find('a')['href']
        except:
            company_link = '---Link is not available---'

        # sorting data
        data_dict = {
            'title': title,
            'company name': company_name,
            'company link': company_link
        }
        job_list.append(data_dict)

    # writing json file
    # 3. create new directory
    try:
        os.mkdir('json_result')
    except FileExistsError:
        pass

    # 4. create file JSON
    with open('json_result/joblist_indeed.json', 'w+') as json_data:
        # 5. using library json = dump
        json.dump(job_list, json_data)
    print('JSON Created')


if __name__ == '__main__':
    get_all_items()
