# 100 Projects in 100 Days
# 
# 
# By Simon A. Betts	13/12/2024

"""
Day 14: Web Scrapping

Method	Description
delete(url, args)	Sends a DELETE request to the specified url
get(url, params, args)	Sends a GET request to the specified url
head(url, args)	Sends a HEAD request to the specified url
patch(url, data, args)	Sends a PATCH request to the specified url
post(url, data, json, args)	Sends a POST request to the specified url
put(url, data, args)	Sends a PUT request to the specified url
request(method, url, args)	Sends a request of the specified method to the specified url

"""

import requests
from bs4 import BeautifulSoup

URL = "https://www.herefordsubaquaclub.com/"
page = requests.get(URL)

soup = BeautifulSoup(page.content,'html.parser')
profile_image = soup.find('img')
print(profile_image)
#soup = BeautifulSoup(html_doc, 'html.parser')
#print(soup.prettify())