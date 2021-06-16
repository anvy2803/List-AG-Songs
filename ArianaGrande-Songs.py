import bs4
from urllib.request import urlopen as ureq
import codecs
from bs4 import BeautifulSoup as soup
import pandas as pd

l1=[]
l2=[]
l3=[]
l4=[]

page_html = codecs.open('songs.html','r')

page_soup = soup(page_html, 'html.parser')

container = page_soup.find_all('tr')

for i in container:
    l1.append(i.th.text.strip())
    l2.append(i.td.text.strip())
    c = i.find_all('td')
    l3.append(c[2].text.strip())
    l4.append(c[3].text.strip())
    
d = {'Song':l1, 'Artist(s)':l2, 'Album':l3, 'Year':l4}
    
lis = pd.DataFrame(d)     
    
lis.to_csv(r'C:\Users\HP\Desktop\songs.csv', index=False) 