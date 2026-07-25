"""
Campaign Payload Builder
"""


def build_campaign_payload(data: dict):

    payload = {
        "name": data["campaign_name"],
        "objective": data["objective"],
        "status": data["status"],
        "buying_type": data["buying_type"],
        "special_ad_categories": [
            data["special_category"]
        ],
    }

    if data["cbo"]:

        if data["budget_type"] == "Daily":

            payload["daily_budget"] = int(data["budget"] * 100)

        else:

            payload["lifetime_budget"] = int(data["budget"] * 100)

    return payload
