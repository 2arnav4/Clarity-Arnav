# File: Backend/utils/fetch_sources.py
# Contains hardcoded news data for demonstration

# IMPORTANT: Generate many more diverse examples here!
hardcoded_news_data = [
    {
        'id': 'hc-1', # Use a prefix like hc- to distinguish if needed
        'headline': 'New Study Shows Coffee Increases Life Expectancy by 20 Years',
        'summary': 'A viral claim suggests drinking coffee daily can extend life by two decades.',
        'status': 'misinformation', # 'verified', 'misinformation', 'unverified'
        'sources': [
            {'name': 'HealthBlog Daily', 'type': 'blog', 'url': '#'},
            {'name': '@healthguru', 'type': 'social', 'url': '#'}
        ],
        'date': '2025-10-19T20:00:00Z', # Use ISO 8601 format preferably
        'originalContent': 'A recent study published in an obscure journal claims that daily coffee consumption can increase life expectancy by 20 years. The study has been widely shared on social media despite lacking peer review.',
        'correction': 'While moderate coffee consumption has been associated with modest health benefits, no credible research supports a 20-year life extension. The original study was not peer-reviewed and used flawed methodology.',
        'breakdown': [
            'The study sample size was only 50 participants',
            'No control group was used',
            'The journal is not recognized by any medical association',
            'Correlation was confused with causation',
            'Results contradict established scientific consensus'
        ]
    },
    {
        'id': 'hc-2',
        'headline': 'NASA Confirms Discovery of Habitable Exoplanet 40 Light Years Away',
        'summary': 'Scientists announce promising findings about potentially Earth-like planet.',
        'status': 'verified',
        'sources': [
            {'name': 'NASA', 'type': 'news', 'url': '#'},
            {'name': 'Science Daily', 'type': 'news', 'url': '#'},
            {'name': 'Nature Astronomy', 'type': 'news', 'url': '#'} # Changed source name slightly
        ],
        'date': '2025-10-19T17:30:00Z',
        'originalContent': 'NASA\'s James Webb Space Telescope has identified strong biosignature candidates on exoplanet K2-18 b, located 120 light years from Earth. The planet orbits within its star\'s habitable zone.',
        'correction': 'This information is accurate. NASA and multiple scientific institutions have confirmed the discovery through peer-reviewed research published in Nature Astronomy.', # Updated correction
        'breakdown': [
            'Confirmed by NASA through official channels',
            'Published in peer-reviewed journal Nature Astronomy', # Updated journal
            'Data collected from James Webb Space Telescope',
            'Multiple independent verification by astronomers',
            'Findings align with established exoplanet detection methods'
        ]
    },
    {
        'id': 'hc-3',
        'headline': '5G Towers Linked to Bird Migration Pattern Changes',
        'summary': 'Claims circulate online connecting cellular infrastructure to wildlife behavior.',
        'status': 'misinformation',
        'sources': [
            {'name': 'r/conspiracy', 'type': 'reddit', 'url': '#'},
            {'name': '@techtruthers', 'type': 'social', 'url': '#'}
        ],
        'date': '2025-10-19T14:15:00Z',
        'originalContent': 'Social media posts claim 5G towers are disrupting bird migration patterns worldwide, citing anecdotal observations and correlating tower installations with bird behavior changes.',
        'correction': 'There is no scientific evidence linking 5G technology to changes in bird migration. Bird migration patterns are influenced by climate change, habitat loss, and natural variations, not electromagnetic radiation from cellular towers at these frequencies.', # Slightly elaborated correction
        'breakdown': [
            'No peer-reviewed studies support this claim',
            '5G frequencies used for mobile networks are non-ionizing', # Clarified frequency type
            'Wildlife agencies report no correlation',
            'Migration changes are well-documented to be climate-related',
            'Similar claims were debunked for 3G and 4G'
        ]
    },
    {
        'id': 'hc-4',
        'headline': 'Local River Shows Unexpected Drop in Pollution Levels After Festival Ban',
        'summary': 'Environmental groups report significant water quality improvement following recent restrictions.',
        'status': 'verified',
        'sources': [
             {'name': 'Local Environmental Agency', 'type': 'news', 'url': '#'},
             {'name': 'City News Hub', 'type': 'news', 'url': '#'}
        ],
        'date': '2025-10-18T10:00:00Z',
        'originalContent': 'Water samples taken from the Yamuna River section near the city show a 40% reduction in key pollutants compared to samples taken before the ban on festival effigy immersions was enforced.',
        'correction': 'Data from the Local Environmental Agency confirms the reported drop in pollutants. While multiple factors affect water quality, the timing strongly correlates with the festival restrictions.',
        'breakdown': [
            'Official water quality reports released by LEA.',
            'Comparison made against pre-ban baseline data.',
            'Specific pollutants measured align with festival waste materials.',
            'Independent environmental groups corroborate findings.',
            'Further studies needed to isolate exact contribution percentages.'
        ]
    },
    {
      'id': 'hc-5',
      'headline': 'Rumors of Hospital Overcrowding Due to Mystery Illness Dismissed by Officials',
      'summary': 'Health Department refutes claims circulating on social media about overwhelmed city hospitals.',
      'status': 'verified', # Officials verified the *refutation*
      'sources': [
          {'name': 'City Health Dept. Press Release', 'type': 'news', 'url': '#'},
          {'name': '@CityHealthAlerts', 'type': 'social', 'url': '#'}
      ],
      'date': '2025-10-17T15:45:00Z',
      'originalContent': 'Posts on WhatsApp and Facebook alleged that several major city hospitals were turning patients away due to a surge in cases of an unidentified respiratory illness following a large public gathering.',
      'correction': 'The City Health Department has issued a statement confirming that while there is a seasonal uptick in respiratory illnesses, hospitals are operating within normal capacity. They urged the public to rely on official sources and avoid spreading unverified information.',
      'breakdown': [
          'Official statement released by the relevant health authority.',
          'Hospital administrators confirmed operational capacity.',
          'No significant increase in admissions reported beyond seasonal norms.',
          'Claims traced back to a small number of unverified social media accounts.',
          'Public health officials advise caution regarding misinformation.'
        ]
    },
    # --- ADD MANY MORE VARIED EXAMPLES HERE ---
    # Include different statuses, sources, dates, and topics.
    # Aim for at least 15-20 diverse items.
    {
        'id': 'hc-6',
        'headline': 'Claim: New Solar Panel Tech Generates Power at Night',
        'summary': 'Article promotes a breakthrough in solar energy, suggesting panels now work in darkness.',
        'status': 'misinformation',
        'sources': [{'name': 'TechFuturist Blog', 'type': 'blog', 'url': '#'}],
        'date': '2025-10-16T09:00:00Z',
        'originalContent': 'A startup claims its revolutionary panels use ambient heat and cosmic rays to generate electricity 24/7, rendering traditional solar obsolete.',
        'correction': 'Current solar photovoltaic technology relies directly on sunlight. While research exists into alternative energy harvesting (like radiative cooling), no commercially viable solar panel generates significant power at night. The claims are unsubstantiated.',
        'breakdown': [
            'Contradicts fundamental principles of photovoltaic effect.',
            'No peer-reviewed research validates the specific claims.',
            'Startup has not demonstrated a working prototype publicly.',
            'Energy physics experts deem the claims highly improbable.',
        ]
    },
    {
        'id': 'hc-7',
        'headline': 'Video Allegedly Shows Politician Accepting Bribe - Authenticity Questioned',
        'summary': 'A grainy video surfaces online purportedly showing a local leader taking cash.',
        'status': 'unverified',
        'sources': [{'name': 'Anonymous Social Media Post', 'type': 'social', 'url': '#'}],
        'date': '2025-10-19T21:30:00Z',
        'originalContent': 'Short video clip circulating shows someone resembling Councilman Sharma accepting an envelope. The source is unknown, and the video quality is poor.',
        'correction': 'The authenticity of the video cannot be confirmed at this time. Experts are analyzing it for signs of manipulation (deepfake). Councilman Sharma has denied the allegations, calling the video a fabrication.',
        'breakdown': [
            'Video source is unverified and anonymous.',
            'Poor video quality makes identification difficult.',
            'Potential for digital manipulation (deepfake) exists.',
            'Subject of the video has issued a strong denial.',
            'No independent corroborating evidence presented yet.'
        ]
    },
    # ... Add more entries ...
]

def get_hardcoded_news():
    """Returns the predefined list of news items."""
    # In a real app, this might fetch from a DB or cache
    # For now, it just returns our hardcoded list
    # print("--- Fetching hardcoded news data ---")
    return hardcoded_news_data

def find_hardcoded_news_by_id(item_id):
    """Finds a specific news item by its ID from the hardcoded list."""
    print(f"--- Searching for hardcoded news item with id: {item_id} ---")
    for item in hardcoded_news_data:
        if item.get('id') == item_id:
            return item
    return None # Return None if not found