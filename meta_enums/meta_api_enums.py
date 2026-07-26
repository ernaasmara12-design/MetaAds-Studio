"""
Meta Marketing API Enums
Seluruh enum resmi Meta digunakan dari file ini.
"""

OBJECTIVES = {
    "Awareness": "OUTCOME_AWARENESS",
    "Traffic": "OUTCOME_TRAFFIC",
    "Engagement": "OUTCOME_ENGAGEMENT",
    "Leads": "OUTCOME_LEADS",
    "App Promotion": "OUTCOME_APP_PROMOTION",
    "Sales": "OUTCOME_SALES",
}

STATUS = {
    "Active": "ACTIVE",
    "Paused": "PAUSED",
}

BILLING_EVENTS = {
    "Impressions": "IMPRESSIONS",
    "Link Clicks": "LINK_CLICKS",
}

OPTIMIZATION_GOALS = {
    "Reach": "REACH",
    "Impressions": "IMPRESSIONS",
    "Link Clicks": "LINK_CLICKS",
    "Landing Page Views": "LANDING_PAGE_VIEWS",
    "Post Engagement": "POST_ENGAGEMENT",
    "Conversions": "OFFSITE_CONVERSIONS",
    "Leads": "LEADS",
    "App Installs": "APP_INSTALLS",
    "ThruPlay": "THRUPLAY",
}

CUSTOM_EVENTS = {
    "Purchase": "PURCHASE",
    "Lead": "LEAD",
    "Add To Cart": "ADD_TO_CART",
    "Initiate Checkout": "INITIATED_CHECKOUT",
    "View Content": "VIEW_CONTENT",
    "Complete Registration": "COMPLETE_REGISTRATION",
    "Search": "SEARCH",
    "Subscribe": "SUBSCRIBE",
}

GENDERS = {
    "All": [],
    "Male": [1],
    "Female": [2],
}

CONVERSION_LOCATIONS = {
    "Website": "WEBSITE",
    "App": "APP",
    "Messenger": "MESSENGER",
    "WhatsApp": "WHATSAPP",
    "Instagram": "INSTAGRAM",
}

DEVICE_PLATFORMS = {
    "Mobile": ["mobile"],
    "Desktop": ["desktop"],
    "All": ["mobile", "desktop"],
}

# ==================================================
# BID STRATEGIES
# ==================================================

BID_STRATEGIES = {
    "Highest Volume": "LOWEST_COST_WITHOUT_CAP",
    "Cost Per Result Goal": "LOWEST_COST_WITH_MIN_ROAS",
    "Bid Cap": "LOWEST_COST_WITH_BID_CAP",
}

# ==================================================
# PUBLISHER PLATFORMS
# ==================================================

PUBLISHER_PLATFORMS = {
    "Facebook": "facebook",
    "Instagram": "instagram",
    "Messenger": "messenger",
    "Audience Network": "audience_network",
}
ADSET_STATUS = {
    "Active": "ACTIVE",
    "Paused": "PAUSED",
}
