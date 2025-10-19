import { useParams, useNavigate } from 'react-router-dom';
import { mockNewsData } from '@/data/mockNews';
import { Header } from '@/components/Header';
import { StatusBadge } from '@/components/StatusBadge';
import { ArrowLeft, ExternalLink, AlertTriangle } from 'lucide-react';
import { Button } from '@/components/ui/button';

const NewsDetail = () => {
  const { id } = useParams();
  const navigate = useNavigate();
  const news = mockNewsData.find(item => item.id === id);

  if (!news) {
    return (
      <div className="min-h-screen bg-background">
        <Header />
        <div className="container mx-auto px-4 py-12 max-w-4xl text-center">
          <h1 className="text-2xl font-bold mb-4">Article not found</h1>
          <Button onClick={() => navigate('/')} variant="outline">
            <ArrowLeft size={16} className="mr-2" />
            Back to feed
          </Button>
        </div>
      </div>
    );
  }

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
            <StatusBadge status={news.status} size="lg" />
          </div>

          {/* Original Content */}
          <section className="mb-8 p-6 rounded-xl border border-border bg-card">
            <h2 className="text-xl font-semibold mb-3 flex items-center gap-2">
              <AlertTriangle size={20} className="text-muted-foreground" />
              Original Claim
            </h2>
            <p className="text-foreground/90 leading-relaxed">
              {news.originalContent}
            </p>
          </section>

          {/* Sources */}
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
                  <span className="text-muted-foreground">({source.type})</span>
                  <ExternalLink size={14} className="text-muted-foreground" />
                </a>
              ))}
            </div>
          </section>

          {/* Fact Check Result */}
          <section className="mb-8 p-6 rounded-xl border-2 border-primary/20 bg-primary/5">
            <h2 className="text-xl font-semibold mb-3">Fact Check</h2>
            <p className="text-foreground/90 leading-relaxed text-lg">
              {news.correction}
            </p>
          </section>

          {/* Breakdown */}
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
