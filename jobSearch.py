import requests
from bs4 import BeautifulSoup
import csv
from datetime import date

#create the url
def get_url(position,location):
    template = "https://de.indeed.com/jobs?q={}&l={}"
    url = template.format(position,location)
    return url

#get the each job posting
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
    record = (jobTitle,company,location,post_date,today,job_salary,summary,job_url)    
    return record

def main(position,location):
    #run the program routine
    records = []
    url = get_url(position,location)

    while True: 
        response = requests.get(url)
        soup = BeautifulSoup(response.content,"html.parser")
        cards = soup.find_all("div",attrs={"jobsearch-SerpJobCard"})
    
        for card in cards:
            record = get_record(card)
            records.append(record) 
        try:
            url =  'https://de.indeed.com/' + soup.find('a',{"aria-label": "Weiter"}).get('href')
            print(url)
        except AttributeError:
            break            
    with open('results.csv','w', newline='',encoding='utf-8') as f:
        writer = csv.writer(f)
        writer.writerow(['Job Title','Company','Location','Post Date','Extract Date','Salary','Summary','url'])
        writer.writerows(records)


#run the program

main('Junior software developer','Berlin')