"""
Meta Ad Set Enums
"""

# Optimization Goal
OPTIMIZATION_GOALS = {
    "Conversions": "OFFSITE_CONVERSIONS",
    "Landing Page Views": "LANDING_PAGE_VIEWS",
    "Link Clicks": "LINK_CLICKS",
    "Reach": "REACH",
    "Impressions": "IMPRESSIONS",
    "Post Engagement": "POST_ENGAGEMENT",
    "ThruPlay": "THRUPLAY",
}

# Billing Event
BILLING_EVENTS = {
    "Impressions": "IMPRESSIONS",
    "Link Clicks": "LINK_CLICKS",
}

# Conversion Location
CONVERSION_LOCATIONS = {
    "Website": "WEBSITE",
    "App": "APP",
    "Messenger": "MESSENGER",
    "Instagram": "INSTAGRAM",
    "WhatsApp": "WHATSAPP",
}

# Dynamic Creative
DYNAMIC_CREATIVE = {
    "On": True,
    "Off": False,
}
