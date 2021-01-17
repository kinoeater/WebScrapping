import requests
from bs4 import BeautifulSoup
import csv

r = requests.get("https://de.indeed.com/jobs?q={}&l={}")

soup = BeautifulSoup(r.content,"lxml")
jobs = soup.find_all("div",attrs={"jobsearch-SerpJobCard"})

for job in jobs:
    print(job.h2.text)
    print(job.find("div",attrs={"class":"location"}).text)
    print(job.find("div",attrs={"class":"summary"}).text)
    print(job.a.href)