import requests         
from bs4 import BeautifulSoup       
res = requests.get('https://news.ycombinator.com/newest')      
soup = BeautifulSoup(res.text, 'html.parser') 
links = soup.select('.storylink')
votes = soup.select('.score')

def create_custom_hn(links, votes):          #hn is hacker news here
  hn = []
  for index,item in enumerate(links):
    title = links[index].getText()
    href = links[index].get('href', None) 
    points = votes[index].getText() 
    print(points)
    print(title)  
    hn.append({'title': title, 'link' : href})
    
  return hn
create_custom_hn(links, votes)
