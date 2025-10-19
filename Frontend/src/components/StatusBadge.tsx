import { NewsStatus } from '@/types/news';
import { CheckCircle, XCircle, AlertCircle } from 'lucide-react';

interface StatusBadgeProps {
  status: NewsStatus;
  size?: 'sm' | 'md' | 'lg';
}

export const StatusBadge = ({ status, size = 'md' }: StatusBadgeProps) => {
  const sizeClasses = {
    sm: 'text-xs px-2 py-1',
    md: 'text-sm px-3 py-1.5',
    lg: 'text-base px-4 py-2'
  };

  const iconSizes = {
    sm: 14,
    md: 16,
    lg: 20
  };

  const config = {
    verified: {
      label: 'Verified',
      className: 'bg-success/10 text-success border-success/20',
      Icon: CheckCircle
    },
    misinformation: {
      label: 'Misinformation',
      className: 'bg-destructive/10 text-destructive border-destructive/20',
      Icon: XCircle
    },
    unverified: {
      label: 'Unverified',
      className: 'bg-warning/10 text-warning border-warning/20',
      Icon: AlertCircle
    }
  };

  const { label, className, Icon } = config[status];

  return (
    <span className={`inline-flex items-center gap-1.5 rounded-full border font-medium ${sizeClasses[size]} ${className}`}>
      <Icon size={iconSizes[size]} />
      {label}
    </span>
  );
};
