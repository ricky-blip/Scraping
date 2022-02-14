import os
from wsgiref import headers
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

#9. Accomodate Company Link
site = 'https://www.indeed.com'
params = {
        'q': 'Python Developer',
        'l': 'New York State',
        '_ga': '2.211888532.1245593939.1644811576-189846848.1644239158',
        'vjk' : 'e401694644bd6752'
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
        'vjk' : 'e401694644bd6752'
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
    
    pagination = soup.find('ul','pagination-list')
    pages = pagination.find_all('li')
    
    for page in pages:
        
        total_pages.append(page.text)
    
    total = int(max(total_pages))
    return total    
    
#1. create function for item job from browser
def get_all_items():
    #2. CoPas parameter
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        '_ga': '2.211888532.1245593939.1644811576-189846848.1644239158',
        'vjk' : 'e401694644bd6752'
    }
    #3. CoPas request
    res = requests.get(url, params=params, headers=headers)
    #4. Check Request per Page
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
    #5. Definition Parser
    soup = BeautifulSoup(res.text, 'html.parser')
    
    # Scraping Process -------------------------
    #6. CoPas Class Job Items from browser
    contents = soup.find_all('table','jobCard_mainContent big6_visualChanges')
    
    #8. Pick Items *title *company name *company link *company address 
    for item in contents:
        title = item.find('h2','jobTitle').text
        company = item.find('span', 'companyName')
        company_name = company.text
        #10. Company have 2 output then use try except
        try:
            company_link = site + company.find('a')['href']
        except:
            company_link = '---Link is not available---'
        print(company_link)
        
#7. Running 
if __name__ == '__main__':
    get_all_items()
    