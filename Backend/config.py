# File: Backend/config.py

import os
from dotenv import load_dotenv

load_dotenv()

# Change the variable name to match .env
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")