import requests
from bs4 import BeautifulSoup
import csv
from datetime import date



def get_url(position,location):
    template = "https://de.indeed.com/jobs?q={}&l={}"
    url = template.format(position,location)
    return url

url = get_url('Software Development python','Berlin')

response = requests.get(url)
#print(response.status_code)
soup = BeautifulSoup(response.content,"html.parser")
#print(soup)
cards = soup.find_all("div",attrs={"jobsearch-SerpJobCard"})
#print(len(jobs))

card = cards[1]
#print(card)

atag = card.h2.a
#print(atag)

jobTitle = atag.get('title')
#print(jobTitle)
job_url = 'https://de.indeed.com/'+ atag.get('href')
#print(job_url)
#companyName= card.find('span','company').text
companyName =card.find("span",attrs={"class":"company"}).text.strip()
city =card.find("div",attrs={"class":"recJobLoc"}).get('data-rc-loc')
summary =card.find("div",attrs={"class":"summary"}).text.strip()
post_date =card.find("span",attrs={"class":"date"}).text.strip()
today = date.today()
#city2 =card.find("span",attrs={"class":"location"}).text
"""print(companyName)
print(city)
print(summary)
print(post_date)
print('today is: '+ str(today))"""

def get_record(card):
    atag = card.h2.a
    jobTitle = atag.get('title')
    job_url = 'https://de.indeed.com/'+ atag.get('href')
    company =card.find("span",attrs={"class":"company"}).text.strip()
    location =card.find("div",attrs={"class":"recJobLoc"}).get('data-rc-loc')
    summary =card.find("div",attrs={"class":"summary"}).text.strip()
    post_date =card.find("span",attrs={"class":"date"}).text.strip()
    today = date.today()
    try: 
        job_salary = card.find("span",attrs={"class":"company"}).text.strip()
    except AttributeError:
        job_salary = ''
    record = (jobTitle,company,city,summary,post_date,today,job_salary,job_url)    
    return record

records = []

for card in cards:
    record = get_record(card)
    records.append(record)

# a = len(soup.find_all('a',{"aria-label": "Weiter"}))
while True: 
    try:
        url =  'https://de.indeed.com/' + soup.find('a',{"aria-label": "Weiter"}).get('href')
        print(url)
    except AttributeError:
        break
    response = requests.get(url)
    soup = BeautifulSoup(response.content,"html.parser")
    cards = soup.find_all("div",attrs={"jobsearch-SerpJobCard"})

    
    for card in cards:
        record = get_record(card)
        records.append(record)

print(len(records))

def main(position,laction):
    records = [] 


    
        





