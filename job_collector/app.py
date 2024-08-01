import os
from flask import Flask, jsonify
from dataclasses import dataclass
from datetime import datetime
from dotenv import load_dotenv, find_dotenv
from sqlalchemy import create_engine, Column, Integer, String, DateTime
from sqlalchemy.orm import declarative_base, sessionmaker
import requests

load_dotenv(find_dotenv())

app = Flask(__name__)

DATABASE_URI = os.getenv('DB_URI')
engine = create_engine(DATABASE_URI)
Session = sessionmaker(bind=engine)
session = Session()
Base = declarative_base()

@dataclass
class Job(Base):
    __tablename__ = 'jobs'

    id:int = Column(Integer, primary_key=True)
    position_id:int = Column(Integer, nullable=False)
    position_title:str = Column(String, nullable=False)
    salary_info:datetime = Column(String)
    posting_date:datetime = Column(DateTime, nullable=False)
    expiration_date:str = Column(DateTime)
    full_county_name:str = Column(String)
    city_name:str = Column(String)
    district_name:str = Column(String)
    job_type_id:int = Column(Integer)
    job_type:str = Column(String)
    fulltime_parttime:str = Column(String)

    def __repr__(self):
        return (f'ID: {self.id}, '
                f'Posting ID: {self.position_id}, '
                f'Position Title: {self.position_title}')

Base.metadata.create_all(engine)

def process_job(job):
    raw_posting_date = int(int(job['postingDate'].strip('/Date()')) / 1000)
    raw_expiration_date = int(int(job['displayUntil'].strip('/Date()')) / 1000)

    posting_date = datetime.fromtimestamp(raw_posting_date)
    expiration_date = datetime.fromtimestamp(raw_expiration_date)

    position_id = job['postingID']
    position_title = job['positionTitle']
    salary_info = job['salaryInfo']
    posting_date = datetime.fromtimestamp(raw_posting_date)
    expiration_date = datetime.fromtimestamp(raw_expiration_date)
    full_county_name = job['fullCountyName']
    city_name = job['city']
    district_name = job['districtName']
    job_type_id = job['jobTypeID']
    job_type = job['jobType']
    fulltime_parttime = job['FullTimePartTime']
    
    job_exists = session.query(Job).filter_by(position_id=position_id).first()

    if job_exists:
        print('Job posting exists in DB')
    else:
        new_job = Job(
            position_id = position_id,
            position_title = position_title,
            salary_info = salary_info,
            posting_date = posting_date,
            expiration_date = expiration_date,
            full_county_name = full_county_name,
            city_name = city_name,
            district_name = district_name,
            job_type_id = job_type_id,
            job_type = job_type,
            fulltime_parttime = fulltime_parttime
            )
        
        session.add(new_job)
        session.commit()
        print("Job did not exist in DB, added to DB")

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

@app.route('/fetch_jobs', methods=['GET'])
def fetch_jobs():
    jobs = session.query(Job).all()
    return jobs

if __name__ == '__main__':
    port = os.getenv('JOB_COLLECTOR_PORT')
    app.run(debug=True, port=port)