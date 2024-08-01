import { CurrentJobs } from "@/pages/currentJobs";

export default function Home() {
  return (
    <main className="flex min-h-screen flex-col items-center justify-between p-24">
      <h1 className="flex flex-col items-center justify-between p-12 w-96 border">Recent Jobs</h1>
      <CurrentJobs />
    </main>
  );
}
