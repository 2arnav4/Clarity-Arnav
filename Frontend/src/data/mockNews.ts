import { NewsItem } from '@/types/news';

export const mockNewsData: NewsItem[] = [
  {
    id: '1',
    headline: 'New Study Shows Coffee Increases Life Expectancy by 20 Years',
    summary: 'A viral claim suggests drinking coffee daily can extend life by two decades.',
    status: 'misinformation',
    sources: [
      { name: 'HealthBlog Daily', type: 'blog', url: '#' },
      { name: '@healthguru', type: 'social', url: '#' }
    ],
    date: '2 hours ago',
    originalContent: 'A recent study published in an obscure journal claims that daily coffee consumption can increase life expectancy by 20 years. The study has been widely shared on social media despite lacking peer review.',
    correction: 'While moderate coffee consumption has been associated with modest health benefits, no credible research supports a 20-year life extension. The original study was not peer-reviewed and used flawed methodology.',
    breakdown: [
      'The study sample size was only 50 participants',
      'No control group was used',
      'The journal is not recognized by any medical association',
      'Correlation was confused with causation',
      'Results contradict established scientific consensus'
    ]
  },
  {
    id: '2',
    headline: 'NASA Confirms Discovery of Habitable Exoplanet 40 Light Years Away',
    summary: 'Scientists announce promising findings about potentially Earth-like planet.',
    status: 'verified',
    sources: [
      { name: 'NASA', type: 'news', url: '#' },
      { name: 'Science Daily', type: 'news', url: '#' },
      { name: 'Nature', type: 'news', url: '#' }
    ],
    date: '5 hours ago',
    originalContent: 'NASA\'s James Webb Space Telescope has identified strong biosignature candidates on exoplanet K2-18 b, located 120 light years from Earth. The planet orbits within its star\'s habitable zone.',
    correction: 'This information is accurate. NASA and multiple scientific institutions have confirmed the discovery through peer-reviewed research.',
    breakdown: [
      'Confirmed by NASA through official channels',
      'Published in peer-reviewed journal Nature',
      'Data collected from James Webb Space Telescope',
      'Multiple independent verification by astronomers',
      'Findings align with established exoplanet detection methods'
    ]
  },
  {
    id: '3',
    headline: '5G Towers Linked to Bird Migration Pattern Changes',
    summary: 'Claims circulate online connecting cellular infrastructure to wildlife behavior.',
    status: 'misinformation',
    sources: [
      { name: 'r/conspiracy', type: 'reddit', url: '#' },
      { name: '@techtruthers', type: 'social', url: '#' }
    ],
    date: '8 hours ago',
    originalContent: 'Social media posts claim 5G towers are disrupting bird migration patterns worldwide, citing anecdotal observations and correlating tower installations with bird behavior changes.',
    correction: 'There is no scientific evidence linking 5G technology to changes in bird migration. Bird migration patterns are influenced by climate change, habitat loss, and natural variations, not electromagnetic radiation from cellular towers.',
    breakdown: [
      'No peer-reviewed studies support this claim',
      '5G frequencies are non-ionizing and safe',
      'Wildlife agencies report no correlation',
      'Migration changes are well-documented to be climate-related',
      'Similar claims were debunked for 3G and 4G'
    ]
  },
  {
    id: '4',
    headline: 'Global Inflation Rate Drops to 3.2% Following Central Bank Coordination',
    summary: 'Economic indicators show declining inflation across major economies.',
    status: 'verified',
    sources: [
      { name: 'Reuters', type: 'news', url: '#' },
      { name: 'Bloomberg', type: 'news', url: '#' },
      { name: 'Financial Times', type: 'news', url: '#' }
    ],
    date: '12 hours ago',
    originalContent: 'Major central banks report coordinated policy measures have successfully reduced global inflation from 8.5% to 3.2% over the past 18 months, according to IMF data.',
    correction: 'This reporting is accurate and based on verified economic data from international financial institutions.',
    breakdown: [
      'Data sourced from IMF official reports',
      'Confirmed by multiple central banks',
      'Published in reputable financial news outlets',
      'Figures match independent economic analyses',
      'Transparent methodology in data collection'
    ]
  },
  {
    id: '5',
    headline: 'Silicon Valley CEO Announces Mind-Reading AI Will Launch Next Month',
    summary: 'Startup claims breakthrough technology can read human thoughts.',
    status: 'misinformation',
    sources: [
      { name: 'TechCrunch wannabe', type: 'blog', url: '#' },
      { name: '@startupnews', type: 'social', url: '#' }
    ],
    date: '1 day ago',
    originalContent: 'A little-known startup CEO announced on social media that their company will launch commercial mind-reading AI technology next month, promising to revolutionize human-computer interaction.',
    correction: 'No such technology exists or is close to commercial release. Current brain-computer interfaces are extremely limited and require invasive procedures. This is likely a marketing stunt or fraud.',
    breakdown: [
      'Company has no published research or patents',
      'Neuroscience experts say technology is decades away',
      'No regulatory approvals or clinical trials',
      'Similar claims have been made and debunked before',
      'CEO has history of exaggerated claims'
    ]
  }
];
