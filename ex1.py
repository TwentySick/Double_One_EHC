import requests
from bs4 import BeautifulSoup

url = "https://dantri.com.vn/the-thao.htm"
#Send a requests to host 
r = requests.get(url)

print(r.status_code) # 200 is success

#print(r.content[:1000]) # print out source code : about 1000 characters

soup = BeautifulSoup(r.content, 'lxml') # Make beautiful source code

print("=========TITLE==========")
# take title of newpapers 
print(soup.title)
# Take text of title of newpaper
print(soup.title.text)

