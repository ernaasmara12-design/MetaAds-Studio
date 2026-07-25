"""
Meta Ads Studio Configuration
"""

import os

APP_NAME = "MetaAds SaaS"
VERSION = "1.0.0"

APP_ID = os.getenv("META_APP_ID", "")
APP_SECRET = os.getenv("META_APP_SECRET", "")
ACCESS_TOKEN = os.getenv("META_ACCESS_TOKEN", "")
AD_ACCOUNT_ID = os.getenv("META_AD_ACCOUNT_ID", "")
API_VERSION = os.getenv("META_API_VERSION", "v24.0")
