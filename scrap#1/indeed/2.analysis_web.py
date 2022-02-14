from wsgiref import headers
import requests
from bs4 import BeautifulSoup

url = 'https://www.indeed.com/jobs?'

#1. copy Query String Parameters from browser 
params = {
        'q': 'Python Developer',
        'l': 'New York State',
        '_ga': '2.211888532.1245593939.1644811576-189846848.1644239158',
        'vjk' : 'e401694644bd6752'
    }

#3. copy User Agent from browser = meaning for website detect us as user not bot
headers = {
    'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/98.0.4758.80 Safari/537.36'
}
 
#2,4. add variable parameters, headers to request
res = requests.get(url, params=params, headers=headers)

#5. check status code
# print(res.status_code)

#6. using beautifulSoup
soup = BeautifulSoup(res.text, 'html.parser')

#7. print raw HTML
print(soup.prettify())