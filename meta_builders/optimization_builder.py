from facebook_business.adobjects.adset import AdSet

from meta_enums.adset import (
    BILLING_EVENTS,
    OPTIMIZATION_GOALS,
)

from meta_enums.campaign import (
    BID_STRATEGIES,
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

    strategy = BID_STRATEGIES.get(
        data.get("bid_strategy")
    )

    if strategy:
        payload[AdSet.Field.bid_strategy] = strategy

    return payload
