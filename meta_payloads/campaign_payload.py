
"""
Meta Marketing API - Campaign Payload Builder
"""

from meta_enums.campaign import (
    OBJECTIVES,
    BUYING_TYPES,
    CAMPAIGN_STATUS,
    BID_STRATEGIES,
    SPECIAL_AD_CATEGORIES,
)


def build_campaign_payload(data: dict) -> dict:
    """
    Build Campaign Payload
    """

    payload = {
        "name": data["name"],
        "objective": data["objective"],
        "status": data.get("status", "PAUSED"),
        "buying_type": data.get("buying_type", "AUCTION"),
        "special_ad_categories": data.get(
            "special_ad_categories",
            []
        ),
    }

    if data.get("daily_budget"):
        payload["daily_budget"] = data["daily_budget"]

    if data.get("lifetime_budget"):
        payload["lifetime_budget"] = data["lifetime_budget"]

    if data.get("bid_strategy"):
        payload["bid_strategy"] = data["bid_strategy"]

    return payload
