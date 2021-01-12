
from bs4 import BeautifulSoup
import requests
import csv
from time import sleep
from random import randint
from datetime import datetime
import pprint

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
    'accept-encoding': 'gzip, deflate, br',
    'accept-language': 'en-US,en;q=0.9',
    'cache-control': 'max-age=0',
    'sec-fetch-dest': 'document',
    'sec-fetch-mode': 'navigate',
    'sec-fetch-site': 'none',
    'sec-fetch-user': '?1',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.67 Safari/537.36 Edg/87.0.664.47'
}

def get_url(position, location):

    '''
    parses indeed and returns the (position, location)

    '''
    template = 'https://www.indeed.com/jobs?q={}&l={}'
    url = template.format(position, location)
    return url

def get_record(card):
    '''
    Extract job data from a single record

    '''
    atag = card.h2.a
    try:
        job_title = atag.get('title')
    except AttributeError:
        job_title = ''
    try:
        company = card.find('span', 'company').text.strip()
    except AttributeError:
        company = ''
    try:
        location = card.find('div', 'recJobLoc').get('data-rc-loc')
    except AttributeError:
        location = ''
    
    
    extract_date = datetime.today().strftime('%Y-%m-%d')
    job_url = 'https://www.indeed.com' + atag.get('href')
    
    return (job_title, company, location, job_url)

def main(position, location, limit=1):
    # Run the main program reouting
    records = []  # creating the record list
    url = get_url(position, location)  # create the url while passing in the position and location.
    
    while True:
        print(url)
        response = requests.get(url, headers=headers)
        soup = BeautifulSoup(response.text, 'html.parser')
        cards = soup.find_all('div', 'jobsearch-SerpJobCard')

        for card in cards:
            record = get_record(card)
            records.append(record)

        try:
            url = 'https://www.indeed.com' + soup.find('a', {'aria-label': 'Next'}).get('href')
            #delay = randint(1, 10)
            #sleep(delay)
        except AttributeError:
            break

         
    with open('results.csv', 'w', newline='', encoding='utf-8') as f:
       writer = csv.writer(f)
       writer.writerow(['Job Title', 'Company', 'Location', 'Job Url'])
       writer.writerows(records)

main('python', 'New York')
