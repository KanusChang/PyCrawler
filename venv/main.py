#import requests
#response = requests.get(
#    "https://travel.ettoday.net/category/%E6%A1%83%E5%9C%92/")

import requests
from bs4 import BeautifulSoup
response = requests.get(
    "https://tw.stock.yahoo.com/s/nine.php/")
soup = BeautifulSoup(response.text, "html.parser")
#print(soup.prettify())  #輸出排版後的HTML內容

#單目標
#result = soup.find("h3")
#print(result)


#多目標
#result = soup.find_all(["h3", "p"], limit=2)
#print(result)

result = soup.find("table")
print(result.select("a"))