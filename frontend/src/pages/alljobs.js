import React, { useState, useEffect } from 'react'

export default function AllJobs() {
    const [jobs, setJobs] = useState([]);

    async function fetchJobs() {
        try {
            console.log('hello')
          const res = await fetch('http://127.0.0.1:5001/fetch_jobs');
          if (!res.ok) {
            throw new Error('Failed to fetch data');
          }
          const data = await res.json();
          console.log(data)
          setJobs(data);
        } catch (error) {
          console.error(error);
        }
      }

    useEffect(() => {
        fetchJobs();
      }, []); 

    return (
        <div>
            <ul className='grid grid-cols-3 gap-4'>
                {jobs.length > 0 ? (
                    jobs.map((job, index) => <li className='border grid-cols-subgrid p-12' key={index}> {job.position_title} </li>)
                ) : (
                    <li>No jobs available</li>
                )}
            </ul>
        </div>
    )
}