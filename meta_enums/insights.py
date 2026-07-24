"""
Meta Marketing API - Insights Enums
"""

# ==========================
# Report Level
# ==========================

LEVEL = {
    "Account": "account",
    "Campaign": "campaign",
    "Ad Set": "adset",
    "Ad": "ad",
}

# ==========================
# Date Preset
# ==========================

DATE_PRESET = {
    "Today": "today",
    "Yesterday": "yesterday",
    "Last 3 Days": "last_3d",
    "Last 7 Days": "last_7d",
    "Last 14 Days": "last_14d",
    "Last 30 Days": "last_30d",
    "Last 90 Days": "last_90d",
    "This Month": "this_month",
    "Last Month": "last_month",
    "Maximum": "maximum",
}

# ==========================
# Attribution
# ==========================

ATTRIBUTION = {
    "1 Day Click": "1d_click",
    "7 Day Click": "7d_click",
    "1 Day View": "1d_view",
    "7 Day Click + 1 Day View": "7d_click,1d_view",
}
