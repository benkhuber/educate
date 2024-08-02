import { FormEvent } from 'react'
import { useRouter } from 'next/router'
 
export default function LoginPage() {
  const router = useRouter()
 
  async function handleSubmit(event) {
    event.preventDefault()
    const formData = new FormData(event.currentTarget)
    const email = formData.get('email')
    const password = formData.get('password')

    const response = await fetch('http://127.0.0.1:5001/api/login', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ email, password }),
    })
 
    if (response.ok) {
      router.push('/dashboard')
    } else {
      console.error('Login failed')
      alert("Invalid email/password")
    }
  }
 
  return (
    <div className='flex min-h-screen flex-col items-center p-24'>
        <form onSubmit={handleSubmit} className='flex flex-col'>
        <input className='text-black' type="email" name="email" placeholder="Email" required />
        <input className='text-black' type="password" name="password" placeholder="Password" required />
        <button type="submit">Login</button>
        </form>
    </div>
  )
}