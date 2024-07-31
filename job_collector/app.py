import os
from flask import Flask
from dotenv import load_dotenv, find_dotenv
import requests

load_dotenv(find_dotenv())

app = Flask(__name__)

def process_job(job):
    posting_id = job["postingID"]
    posting_title = job["positionTitle"]
    print(f"{posting_id}: {posting_title}")

@app.route('/')
def home():
    return 'Job Collector Server'

@app.route('/collector')
def collector():
    url = os.getenv('EDJOIN_API_URL')

    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        jobs = data["data"]

        for job in jobs:
            process_job(job)
    
    else:
        print(f"Request failed: {response.status_code}")
        return (f"Request failed: {response.status_code}")

    return f"Status: {response.status_code}, collecting jobs..."

if __name__ == '__main__':
    app.run(debug=True)