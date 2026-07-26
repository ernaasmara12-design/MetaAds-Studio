from facebook_business.adobjects.adset import AdSet


def build_adset_payload(data):

    payload = {

        AdSet.Field.name:
            data["adset_name"],

        AdSet.Field.campaign_id:
            data["campaign_id"],

        AdSet.Field.status:
            "PAUSED",

    }

    if data["budget_type"] == "Daily Budget":

        payload[AdSet.Field.daily_budget] = int(
            data["budget"] * 100
        )

    else:

        payload[AdSet.Field.lifetime_budget] = int(
            data["budget"] * 100
        )

    return payload
