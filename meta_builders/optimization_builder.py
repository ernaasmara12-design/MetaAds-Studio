from facebook_business.adobjects.adset import AdSet

from meta_enums.adset import (
    BILLING_EVENTS,
    OPTIMIZATION_GOALS,
)


def build_optimization(data):

    payload = {}

    billing = BILLING_EVENTS.get(
        data.get("billing_event")
    )

    if billing:
        payload[AdSet.Field.billing_event] = billing

    optimization = OPTIMIZATION_GOALS.get(
        data.get("optimization_goal")
    )

    if optimization:
        payload[AdSet.Field.optimization_goal] = optimization

    bid_strategy = data.get("bid_strategy")

    if bid_strategy:
        payload[AdSet.Field.bid_strategy] = bid_strategy

    return payload
