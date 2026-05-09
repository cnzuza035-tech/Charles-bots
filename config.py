# Configuration file for Charles Bots
# IMPORTANT: Never commit sensitive credentials to GitHub!
# Use environment variables instead

import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# ============ INSTAGRAM CONFIGURATION ============
INSTAGRAM_USERNAME = os.getenv("INSTAGRAM_USERNAME", "")
INSTAGRAM_PASSWORD = os.getenv("INSTAGRAM_PASSWORD", "")
INSTAGRAM_SESSIONS = 5  # Number of concurrent sessions
INSTAGRAM_DELAY = 60  # Delay between actions (seconds)

# ============ TWITTER CONFIGURATION ============
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY", "")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET", "")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN", "")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET", "")
TWITTER_BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN", "")
TWITTER_DELAY = 45

# ============ TIKTOK CONFIGURATION ============
TIKTOK_USERNAME = os.getenv("TIKTOK_USERNAME", "")
TIKTOK_PASSWORD = os.getenv("TIKTOK_PASSWORD", "")
TIKTOK_DELAY = 60

# ============ FACEBOOK CONFIGURATION ============
FACEBOOK_ACCESS_TOKEN = os.getenv("FACEBOOK_ACCESS_TOKEN", "")
FACEBOOK_PAGE_ID = os.getenv("FACEBOOK_PAGE_ID", "")
FACEBOOK_DELAY = 30

# ============ LINKEDIN CONFIGURATION ============
LINKEDIN_EMAIL = os.getenv("LINKEDIN_EMAIL", "")
LINKEDIN_PASSWORD = os.getenv("LINKEDIN_PASSWORD", "")
LINKEDIN_DELAY = 45

# ============ PROXY CONFIGURATION ============
USE_PROXY = os.getenv("USE_PROXY", "false").lower() == "true"
PROXY_LIST = os.getenv("PROXY_LIST", "").split(",")
ROTATE_PROXY = True

# ============ DATABASE CONFIGURATION ============
DATABASE_URL = os.getenv("DATABASE_URL", "sqlite:///bots.db")

# ============ LOGGING CONFIGURATION ============
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = "logs/charles_bots.log"

# ============ SCHEDULING CONFIGURATION ============
SCHEDULE_ENABLED = True
CHECK_INTERVAL = 300  # Check scheduler every 5 minutes

# ============ SAFETY LIMITS ============
MAX_ACTIONS_PER_DAY = 500  # Maximum actions per day per account
MIN_DELAY_BETWEEN_ACTIONS = 5  # Minimum delay between actions (seconds)
MAX_ACCOUNTS = 10  # Maximum concurrent accounts

# ============ FEATURE FLAGS ============
ENABLE_INSTAGRAM = True
ENABLE_TWITTER = True
ENABLE_TIKTOK = True
ENABLE_FACEBOOK = True
ENABLE_LINKEDIN = True

# ============ AUTOMATION RULES ============
# Add your automation rules here
AUTOMATION_CONFIG = {
    "follow_hashtags": ["python", "coding", "tech"],
    "follow_users": [],
    "auto_like": True,
    "auto_comment": True,
    "auto_follow": True,
    "batch_size": 10,
}
