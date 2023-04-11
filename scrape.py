from bs4 import BeautifulSoup
import requests
from csv import writer
from datetime import date
today = date.today()
import csv
try:
    reader = csv.reader(open('ddmmyyy_verge.csv'))
    number = len(list(reader))
    number = number-1
    # print(number)
except:
    number = 0
    with open("ddmmyyy_verge.csv", 'a', encoding='utf8', newline ='') as f:
        thewriter = writer(f)
        header = ['ID', 'URL', 'Headline', 'Author', 'Date']
        thewriter.writerow(header)

base_url = "https://www.theverge.com/"
page = requests.get(base_url)

soup = BeautifulSoup(page.content, 'html.parser')

op = soup.find_all('ol', class_ = "relative")
lists = op[0].find_all('li')
# print(len(lists))

with open("ddmmyyy_verge.csv", 'a', encoding='utf8', newline ='') as f:
    thewriter = writer(f)
    # header = ['ID', 'URL', 'Headline', 'Author', 'Date']
    # thewriter.writerow(header)
    
    for list in lists:
        id       = number
        sideurl      = list.find('a', class_ ="group-hover:shadow-underline-franklin").get('href')
        url     = base_url + sideurl
        headline = list.find('a', class_ = "group-hover:shadow-underline-franklin").text.replace('\n', '')
        author   = list.find('a', class_ ="text-gray-31 hover:shadow-underline-inherit dark:text-franklin mr-8").text.replace('\n', '')
        # date     = list.find('span', class_ = 'text-gray-63 dark:text-gray-94').text.replace('\n', '')
        date     = today.strftime("%B %d").replace('\n', '')
        info     = [id, url, headline, author, date]
        thewriter.writerow(info)
        number = number + 1
import duplicates
import exporting_storedb
import os
# file = 'temp.csv'
# if(os.path.exists(file) and os.path.isfile(file)):
#     os.close(file)
# os.close("temp.csv")
# os.remove("temp.csv")