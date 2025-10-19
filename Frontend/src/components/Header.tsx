import { ShieldCheck } from 'lucide-react';
import { useNavigate } from 'react-router-dom';

export const Header = () => {
  const navigate = useNavigate();

  return (
    <header className="border-b border-border bg-background/95 backdrop-blur supports-[backdrop-filter]:bg-background/60 sticky top-0 z-50">
      <div className="container mx-auto px-4 py-4 max-w-4xl">
        <div
          onClick={() => navigate('/')}
          className="flex items-center gap-3 cursor-pointer group"
        >
          <ShieldCheck className="text-primary group-hover:scale-110 transition-transform" size={32} />
          <div>
            <h1 className="text-2xl font-bold text-foreground">FactCheck</h1>
            <p className="text-xs text-muted-foreground">Truth in the noise</p>
          </div>
        </div>
      </div>
    </header>
  );
};
