from facebook_business.adobjects.adset import AdSet


def build_budget(data):

    payload = {}

    budget = data.get("budget")

    if not budget:
        return payload

    budget = int(float(budget) * 100)

    if data.get("budget_type") == "Daily Budget":
        payload[AdSet.Field.daily_budget] = budget
    else:
        payload[AdSet.Field.lifetime_budget] = budget

    return payload
