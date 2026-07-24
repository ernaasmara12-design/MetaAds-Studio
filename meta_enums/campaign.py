"""
Meta Campaign Enums
"""

# Campaign Objective
OBJECTIVES = {
    "Awareness": "OUTCOME_AWARENESS",
    "Traffic": "OUTCOME_TRAFFIC",
    "Engagement": "OUTCOME_ENGAGEMENT",
    "Leads": "OUTCOME_LEADS",
    "App Promotion": "OUTCOME_APP_PROMOTION",
    "Sales": "OUTCOME_SALES",
}

# Campaign Status
STATUS = {
    "Active": "ACTIVE",
    "Paused": "PAUSED",
    "Archived": "ARCHIVED",
}

# Buying Type
BUYING_TYPES = {
    "Auction": "AUCTION",
}

# Budget Type
BUDGET_TYPES = {
    "Daily Budget": "daily_budget",
    "Lifetime Budget": "lifetime_budget",
}

# Bid Strategy
BID_STRATEGIES = {
    "Lowest Cost": "LOWEST_COST_WITHOUT_CAP",
    "Cost Cap": "COST_CAP",
    "Bid Cap": "BID_CAP",
}

# Special Ad Category
SPECIAL_AD_CATEGORIES = {
    "None": [],
    "Credit": ["CREDIT"],
    "Employment": ["EMPLOYMENT"],
    "Housing": ["HOUSING"],
}
