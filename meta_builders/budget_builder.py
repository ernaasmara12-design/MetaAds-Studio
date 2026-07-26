from facebook_business.adobjects.adset import AdSet


def build_budget(data):

    payload = {}

    budget = int(float(data["budget"]) * 100)

    if data["budget_type"] == "Daily Budget":
        payload[AdSet.Field.daily_budget] = budget
    else:
        payload[AdSet.Field.lifetime_budget] = budget

    return payload
