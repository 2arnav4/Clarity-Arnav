import { mockNewsData } from '@/data/mockNews';
import { NewsCard } from '@/components/NewsCard';
import { Header } from '@/components/Header';

const Index = () => {
  return (
    <div className="min-h-screen bg-background">
      <Header />
      
      <main className="container mx-auto px-4 py-8 max-w-4xl">
        <div className="mb-8">
          <h2 className="text-2xl font-bold text-foreground mb-2">Trending News</h2>
          <p className="text-muted-foreground">
            Real-time fact-checking of viral stories from across the web
          </p>
        </div>

        <div className="space-y-4">
          {mockNewsData.map(news => (
            <NewsCard key={news.id} news={news} />
          ))}
        </div>
      </main>
    </div>
  );
};

export default Index;
