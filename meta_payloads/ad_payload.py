
"""
Meta Marketing API - Ad Payload Builder
"""


def build_ad_payload(data: dict) -> dict:
    """
    Build Ad Payload
    """

    payload = {
        "name": data["name"],
        "adset_id": data["adset_id"],
        "creative": {
            "creative_id": data["creative_id"]
        },
        "status": data.get("status", "PAUSED"),
    }

    if data.get("tracking_specs"):
        payload["tracking_specs"] = data["tracking_specs"]

    if data.get("conversion_domain"):
        payload["conversion_domain"] = data["conversion_domain"]

    if data.get("bid_amount"):
        payload["bid_amount"] = data["bid_amount"]

    return payload
