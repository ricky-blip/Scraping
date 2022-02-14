#1. import library
import requests
from bs4 import BeautifulSoup

#2. copy request url from browser
url = 'https://www.indeed.com/jobs?'

#3. check request and run
res = requests.get(url)

#4. check status code *must be same from browse, after that we can scrap di website
print(res.status_code)