"""
Campaign Payload Builder
"""

from meta_enums.campaign import (
    OBJECTIVES,
    STATUS,
    BUDGET_TYPES,
    BID_STRATEGIES,
    SPECIAL_AD_CATEGORIES,
)


def build_campaign_payload(data: dict):

    payload = {
    "name": data["campaign_name"],
    "objective": OBJECTIVES[data["objective"]],
    "status": STATUS[data["status"]],
    "special_ad_categories": SPECIAL_AD_CATEGORIES[data["special_category"]],
}
    # Budget (CBO)
    if data["cbo"]:

        budget_field = BUDGET_TYPES[data["budget_type"]]

        payload[budget_field] = int(data["budget"] * 100)

    # Bid Strategy (opsional)
    if data.get("bid_strategy"):
        payload["bid_strategy"] = BID_STRATEGIES[data["bid_strategy"]]

    return payload
