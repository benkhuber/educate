import React from 'react'

export const CurrentJobs = () => {
    async function fetchJobs() {
        const res = await fetch('http://127.0.0.1:5001/fetch_jobs')
    
        if (!res.ok) {
          throw new Error('Failed to fetch data')
        }
        
        const data = await res.json()
        console.log(data)
    
        return "yessir"
    }
    
    fetchJobs()

    return (
        <div>CurrentJobs</div>
    )
}
