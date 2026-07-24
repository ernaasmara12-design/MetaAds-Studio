"""
Meta Marketing API - Ad Set Payload Builder
"""

from meta_enums.adset import (
    OPTIMIZATION_GOALS,
    BILLING_EVENTS,
    DESTINATION_TYPES,
    PERFORMANCE_GOALS,
)


def build_adset_payload(data: dict) -> dict:
    """
    Build Ad Set Payload
    """

    payload = {
        "name": data["name"],
        "campaign_id": data["campaign_id"],
        "status": data.get("status", "PAUSED"),
        "daily_budget": data.get("daily_budget"),
        "lifetime_budget": data.get("lifetime_budget"),
        "billing_event": data["billing_event"],
        "optimization_goal": data["optimization_goal"],
        "destination_type": data["destination_type"],
        "performance_goal": data.get("performance_goal"),
    }

    if data.get("start_time"):
        payload["start_time"] = data["start_time"]

    if data.get("end_time"):
        payload["end_time"] = data["end_time"]

    if data.get("targeting"):
        payload["targeting"] = data["targeting"]

    if data.get("promoted_object"):
        payload["promoted_object"] = data["promoted_object"]

    if data.get("bid_amount"):
        payload["bid_amount"] = data["bid_amount"]

    return payload
