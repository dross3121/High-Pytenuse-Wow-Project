import csv
from flask import Flask, render_template


app = Flask(__name__)


def parseCSVFile():
    ''' 
    returns data from merged.csv flat file using the with open function to render the data from a csv file 
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
    '''
    returns idex page template
    '''
    return render_template('home.html') 


@app.route('/about/')
def about():
    '''
    returns about page template
    '''
    return render_template('about.html')


@app.route('/jobs/')
def jobs():
    '''
    Returns data from merged.csv formatted with columns job title,company, location, and url  
    '''
    return render_template('jobs.html', githubjob= parseCSVFile())

            



if __name__ == '__main__':
    app.run()
