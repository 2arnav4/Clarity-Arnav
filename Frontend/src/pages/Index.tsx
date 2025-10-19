// File: Frontend/src/pages/Index.tsx

// Remove mock data import:
// import { mockNewsData } from '@/data/mockNews';
import { NewsCard } from '@/components/NewsCard';
import { Header } from '@/components/Header';
import { useQuery } from '@tanstack/react-query'; // Import useQuery
import { NewsItem } from '@/types/news'; // Import the type
import { Skeleton } from '@/components/ui/skeleton'; // For loading state
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'; // For error state
import { Terminal } from 'lucide-react';

// Define the shape of the API response
interface NewsApiResponse {
  articles: NewsItem[];
  fetch_errors?: string[] | null; // Match backend response
}

// Function to fetch news from the backend
const fetchNews = async (): Promise<NewsApiResponse> => {
  // Ensure your backend is running, likely on port 5000
  const response = await fetch('http://localhost:5000/api/news/trending'); // Use correct backend URL
  if (!response.ok) {
    // Try to get error message from backend response
    let errorMsg = `HTTP error! status: ${response.status}`;
    try {
        const errData = await response.json();
        errorMsg = errData.error || errorMsg;
    } catch (e) { /* Ignore if response is not JSON */ }
    throw new Error(errorMsg);
  }
  return response.json();
};


const Index = () => {
  // Use React Query to fetch data
  const { data, isLoading, isError, error } = useQuery<NewsApiResponse, Error>({
    queryKey: ['trendingNews'], // Unique key for this query
    queryFn: fetchNews, // The function to fetch data
    // Optional: Add staleTime or cacheTime if needed
    // staleTime: 5 * 60 * 1000, // 5 minutes
  });

  return (
    <div className="min-h-screen bg-background">
      <Header />

      <main className="container mx-auto px-4 py-8 max-w-4xl">
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-foreground mb-2">Trending News</h2>
          <p className="text-muted-foreground">
            {/* Updated description */}
            Insights on current events and viral stories
          </p>
        </div>

        {/* Loading State */}
        {isLoading && (
          <div className="space-y-4">
            <Skeleton className="h-36 w-full rounded-xl" />
            <Skeleton className="h-36 w-full rounded-xl" />
            <Skeleton className="h-36 w-full rounded-xl" />
          </div>
        )}

        {/* Error State */}
        {isError && (
          <Alert variant="destructive">
            <Terminal className="h-4 w-4" />
            <AlertTitle>Error Fetching News</AlertTitle>
            <AlertDescription>
              {error?.message || 'Could not load trending news. Please try again later.'}
            </AlertDescription>
          </Alert>
        )}

        {/* Success State */}
        {data && data.articles && !isLoading && !isError && (
          <div className="space-y-4">
            {data.articles.length === 0 ? (
              <p className="text-muted-foreground text-center">No news items available right now.</p>
            ) : (
               data.articles.map(news => (
                <NewsCard key={news.id} news={news} />
              ))
            )}
            {/* Optionally display fetch errors if backend includes them */}
            {data.fetch_errors && (
               <Alert variant="destructive" className="mt-4">
                 <Terminal className="h-4 w-4" />
                 <AlertTitle>Data Fetching Issues</AlertTitle>
                 <AlertDescription>
                   Could not fetch data from all sources: {data.fetch_errors.join('; ')}
                 </AlertDescription>
               </Alert>
            )}
          </div>
        )}
      </main>
    </div>
  );
};

export default Index;