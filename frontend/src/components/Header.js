import Link from 'next/link'

export default function Header() {
    return (
      <div className='flex flex-row justify-between p-12'>
                <Link href='/'>EDUCATE</Link>
                <div className='flex flex-row gap-5'>
                    <Link href='/login'>Login</Link>
                    <Link href="/alljobs">All Jobs</Link> 
                </div> 
      </div>
    )
  }