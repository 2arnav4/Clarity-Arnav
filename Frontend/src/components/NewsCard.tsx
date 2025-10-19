import { NewsItem } from '@/types/news';
import { StatusBadge } from './StatusBadge';
import { Clock } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

interface NewsCardProps {
  news: NewsItem;
}

export const NewsCard = ({ news }: NewsCardProps) => {
  const navigate = useNavigate();

  return (
    <article
      onClick={() => navigate(`/news/${news.id}`)}
      className="group cursor-pointer rounded-xl border border-border bg-card p-6 transition-all hover:border-primary/50 hover:shadow-lg hover:shadow-primary/5 animate-fade-in"
    >
      <div className="flex items-start justify-between gap-4 mb-4">
        <h2 className="text-xl font-semibold text-foreground group-hover:text-primary transition-colors leading-tight">
          {news.headline}
        </h2>
        <StatusBadge status={news.status} size="sm" />
      </div>

      <p className="text-muted-foreground mb-4 line-clamp-2">
        {news.summary}
      </p>

      <div className="flex items-center justify-between text-sm text-muted-foreground">
        <div className="flex items-center gap-2">
          <Clock size={14} />
          <span>{news.date}</span>
        </div>
        <div className="flex items-center gap-2">
          <span className="text-xs">
            {news.sources.length} {news.sources.length === 1 ? 'source' : 'sources'}
          </span>
        </div>
      </div>
    </article>
  );
};
