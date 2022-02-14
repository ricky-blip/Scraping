import os
from wsgiref import headers
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

params = {
        'q': 'Python Developer',
        'l': 'New York State',
        '_ga': '2.211888532.1245593939.1644811576-189846848.1644239158',
        'vjk' : 'e401694644bd6752'
    }

headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
}

# check status code
# print(res.status_code)
res = requests.get(url, params=params, headers=headers)


#1. looking ending pagination website -> create function for total page -> move params to this function -> do request -> compare with library os
def get_totalpages():
    params = {
        'q': 'Python Developer',
        'l': 'New York State',
        '_ga': '2.211888532.1245593939.1644811576-189846848.1644239158',
        'vjk' : 'e401694644bd6752'
    }
    
    res = requests.get(url, params=params, headers=headers)
    
    #2. create new directory for temporary result file scraping
    try:
        os.mkdir('temp')
    except FileExistsError:
        pass
    
    #3. create html for html-raw we get
    with open('temp/res.html', 'w+') as outfile:
        outfile.write(res.text)
        outfile.close()
        
    #9. accomodate all page with [list]
    total_pages = []
        
    #4. definiton Soup for Scraping step
    soup = BeautifulSoup(res.text, 'html.parser')
    
    #6. get ul from pagination
    pagination = soup.find('ul','pagination-list')
    #7. get li from pagination
    pages = pagination.find_all('li')
    #8. get number page from pagination
    for page in pages:
        # print(page.text)
        total_pages.append(page.text)
    # print(total_pages) # print list page
    
    #10. looking for max page/end page/
    total = int(max(total_pages))
    return total    
    
#5. running file
if __name__ == '__main__':
    get_totalpages()
    