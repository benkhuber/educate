from flask import Flask
import requests
import json

app = Flask(__name__)

def process_job(job):
    posting_id = job["postingID"]
    print(posting_id)

@app.route('/')
def home():
    return 'Job_collector'

@app.route('/collector')
def collector():
    url = 'https://www.edjoin.org/Home/LoadJobs?rows=50&page=1&sort=postingDate&sortVal=2&order=desc&keywords=&location=&searchType=&regions=30&jobTypes=2,3,48,64,1,63&days=undefined&empType=&catID=0&onlineApps=true&recruitmentCenterID=0&stateID=24&regionID=null&districtID=0&searchID=0&_=1722384394646'

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        jobs = data["data"]

        for job in jobs:
            process_job(job)
    
    else:
        print(f"Request failed: {response.status_code}")
    return 'Collecting jobs...'

if __name__ == '__main__':
    app.run(debug=True)