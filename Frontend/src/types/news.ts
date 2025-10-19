export type NewsStatus = 'verified' | 'misinformation' | 'unverified';

export interface NewsSource {
  name: string;
  type: 'news' | 'blog' | 'social' | 'reddit';
  url: string;
}

export interface NewsItem {
  id: string;
  headline: string;
  summary: string;
  status: NewsStatus;
  sources: NewsSource[];
  date: string;
  correction?: string;
  breakdown?: string[];
  originalContent?: string;
}
