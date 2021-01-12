import requests 
from flask import Flask, render_template, jsonify
import csv

app = Flask(__name__)

# def githubjobs():  


#     page = 1
#     more_pages = True
#     title = 'title'
#     company = 'company'
#     url = 'url'
#     location = 'location'
#     all_data = []

#     while more_pages:

#         r= requests.get(f'https://jobs.github.com/positions.json?page={page}')

#         for HPS in r.json():
#             results = {
#             "Company" : HPS[company],
#             "Title": HPS[title],
#             "Location": HPS[location],
#              "Url": HPS[url]

#             }
#             all_data.append(results)

#         nextpage= requests.get(f'https://jobs.github.com/positions.json?page={page+1}')

#         if len(nextpage.json()) == 0:
#             more_pages = False


#         page+=1 
#     return all_data


def parseCSVFile():
    ''' 
    returns data from merged.csv flat file database 
    '''


    data =[]

    with open('merged.csv', newline='') as f:
        reader = csv.DictReader(f)
        print('reading file')
        for row in reader:
            data.append(row)
        return data  



@app.route('/')
def home():

    return render_template('home.html') 


@app.route('/about/')
def about():

    return render_template('about.html')


@app.route('/jobs/')
def jobs():
    # githubjob= githubjobs()
    print(parseCSVFile())
    '''
    Dispalys data from merged.csv
    '''

    return render_template('jobs.html', githubjob= parseCSVFile())

            



if __name__ == '__main__':
    app.run()
