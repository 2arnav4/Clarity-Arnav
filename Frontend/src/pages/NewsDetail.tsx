// File: Frontend/src/pages/NewsDetail.tsx

import { useParams, useNavigate } from 'react-router-dom';
// Remove mock data import:
// import { mockNewsData } from '@/data/mockNews';
import { Header } from '@/components/Header';
import { StatusBadge } from '@/components/StatusBadge';
import { ArrowLeft, ExternalLink, AlertTriangle, Terminal } from 'lucide-react';
import { Button } from '@/components/ui/button';
import { useQuery } from '@tanstack/react-query'; // Import useQuery
import { NewsItem } from '@/types/news'; // Import the type
import { Skeleton } from '@/components/ui/skeleton'; // For loading state
import { Alert, AlertDescription, AlertTitle } from '@/components/ui/alert'; // For error state

// Function to fetch a single news item by ID from the backend
const fetchNewsById = async (id: string | undefined): Promise<NewsItem | null> => {
  if (!id) {
    // Handle case where ID might be undefined initially
    return null; // Or throw an error, depending on desired behavior
  }
  const response = await fetch(`http://localhost:5000/api/news/${id}`); // Use correct backend URL
  if (response.status === 404) {
      return null; // Explicitly handle not found
  }
  if (!response.ok) {
     let errorMsg = `HTTP error! status: ${response.status}`;
     try {
        const errData = await response.json();
        errorMsg = errData.error || errorMsg;
    } catch (e) { /* Ignore */ }
    throw new Error(errorMsg);
  }
  return response.json();
};

const NewsDetail = () => {
  const { id } = useParams<{ id: string }>(); // Get ID from URL params
  const navigate = useNavigate();

  // Use React Query to fetch the specific news item
  const { data: news, isLoading, isError, error, isSuccess } = useQuery<NewsItem | null, Error>({
      queryKey: ['newsDetail', id], // Include ID in the query key
      queryFn: () => fetchNewsById(id),
      enabled: !!id, // Only run the query if ID exists
  });

  // Loading State
  if (isLoading) {
    return (
      <div className="min-h-screen bg-background">
        <Header />
        <main className="container mx-auto px-4 py-8 max-w-4xl">
           <Skeleton className="h-8 w-24 mb-6" />
           <Skeleton className="h-16 w-3/4 mb-4" />
           <Skeleton className="h-6 w-20 mb-8" />
           <Skeleton className="h-24 w-full mb-8 rounded-xl" />
           <Skeleton className="h-10 w-full mb-8 rounded-xl" />
           <Skeleton className="h-32 w-full mb-8 rounded-xl" />
        </main>
      </div>
    );
  }

  // Error State
  if (isError) {
      return (
        <div className="min-h-screen bg-background">
          <Header />
          <div className="container mx-auto px-4 py-12 max-w-4xl text-center">
            <Alert variant="destructive" className="text-left mb-4">
              <Terminal className="h-4 w-4" />
              <AlertTitle>Error Loading Article</AlertTitle>
              <AlertDescription>
                {error?.message || 'Could not load the article details.'}
              </AlertDescription>
            </Alert>
            <Button onClick={() => navigate('/')} variant="outline">
              <ArrowLeft size={16} className="mr-2" />
              Back to feed
            </Button>
          </div>
        </div>
      );
  }

  // Not Found State (check after loading and success)
  if (isSuccess && !news) {
    return (
      <div className="min-h-screen bg-background">
        <Header />
        <div className="container mx-auto px-4 py-12 max-w-4xl text-center">
          <h1 className="text-2xl font-bold mb-4">Article not found</h1>
          <p className="text-muted-foreground mb-4">The article with ID '{id}' does not exist.</p>
          <Button onClick={() => navigate('/')} variant="outline">
            <ArrowLeft size={16} className="mr-2" />
            Back to feed
          </Button>
        </div>
      </div>
    );
  }

  // --- Render article details using fetched 'news' data ---
  // Ensure news is not null before accessing properties
  if (!news) return null; // Should ideally be caught by previous checks, but good for safety

  return (
    <div className="min-h-screen bg-background">
      <Header />

      <main className="container mx-auto px-4 py-8 max-w-4xl">
        <Button
          onClick={() => navigate('/')}
          variant="ghost"
          className="mb-6"
        >
          <ArrowLeft size={16} className="mr-2" />
          Back to feed
        </Button>

        <article className="animate-fade-in">
          {/* Headline and Status */}
          <div className="mb-8">
            <div className="flex items-start justify-between gap-4 mb-4">
              <h1 className="text-3xl md:text-4xl font-bold text-foreground leading-tight">
                {news.headline}
              </h1>
            </div>
            {/* Ensure status exists before rendering badge */}
            {news.status && <StatusBadge status={news.status} size="lg" />}
          </div>

          {/* Original Content */}
          {news.originalContent && (
             <section className="mb-8 p-6 rounded-xl border border-border bg-card">
              <h2 className="text-xl font-semibold mb-3 flex items-center gap-2">
                <AlertTriangle size={20} className="text-muted-foreground" />
                Original Claim
              </h2>
              <p className="text-foreground/90 leading-relaxed">
                {news.originalContent}
              </p>
            </section>
          )}


          {/* Sources */}
          {news.sources && news.sources.length > 0 && (
              <section className="mb-8">
              <h2 className="text-xl font-semibold mb-4">Sources</h2>
              <div className="flex flex-wrap gap-3">
                {news.sources.map((source, idx) => (
                  <a
                    key={idx}
                    href={source.url}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="inline-flex items-center gap-2 px-4 py-2 rounded-lg border border-border bg-card text-sm hover:border-primary/50 transition-colors"
                  >
                    <span className="font-medium">{source.name}</span>
                    {/* Only show type if it exists */}
                    {source.type && <span className="text-muted-foreground">({source.type})</span>}
                    <ExternalLink size={14} className="text-muted-foreground" />
                  </a>
                ))}
              </div>
            </section>
          )}


          {/* Fact Check Result */}
           {news.correction && (
              <section className="mb-8 p-6 rounded-xl border-2 border-primary/20 bg-primary/5">
                <h2 className="text-xl font-semibold mb-3">Fact Check / Correction</h2>
                <p className="text-foreground/90 leading-relaxed text-lg">
                  {news.correction}
                </p>
              </section>
           )}


          {/* Breakdown / Why This Matters */}
          {news.breakdown && news.breakdown.length > 0 && (
            <section className="mb-8">
              <h2 className="text-xl font-semibold mb-4">Why This Matters</h2>
              <ul className="space-y-3">
                {news.breakdown.map((point, idx) => (
                  <li
                    key={idx}
                    className="flex items-start gap-3 p-4 rounded-lg bg-card border border-border"
                  >
                    <span className="flex-shrink-0 w-6 h-6 rounded-full bg-primary/10 text-primary flex items-center justify-center text-sm font-semibold">
                      {idx + 1}
                    </span>
                    <span className="text-foreground/90 leading-relaxed">{point}</span>
                  </li>
                ))}
              </ul>
            </section>
          )}
        </article>
      </main>
    </div>
  );
};

export default NewsDetail;