from datetime import datetime

from facebook_business.adobjects.adset import AdSet

from meta_enums.adset import (
    BILLING_EVENTS,
    OPTIMIZATION_GOALS,
)


def build_adset_payload(data):

    payload = {
        AdSet.Field.name: data["adset_name"],
        AdSet.Field.campaign_id: data["campaign_id"],
        AdSet.Field.status: "PAUSED",
    }

    # ======================================
    # Budget
    # ======================================

    if data["budget_type"] == "Daily Budget":
        payload[AdSet.Field.daily_budget] = int(data["budget"] * 100)
    else:
        payload[AdSet.Field.lifetime_budget] = int(data["budget"] * 100)

    # ======================================
    # Billing Event
    # ======================================

    billing_event = BILLING_EVENTS.get(
        data.get("billing_event")
    )

    if billing_event:
        payload[AdSet.Field.billing_event] = billing_event

    # ======================================
    # Optimization Goal
    # ======================================

    optimization_goal = OPTIMIZATION_GOALS.get(
        data.get("optimization_goal")
    )

    if optimization_goal:
        payload[AdSet.Field.optimization_goal] = optimization_goal

    # ======================================
    # Schedule
    # ======================================

    start_date = data.get("start_date")
    start_time = data.get("start_time")

    if start_date and start_time:

        payload[AdSet.Field.start_time] = datetime.combine(
            start_date,
            start_time,
        ).isoformat()

    end_date = data.get("end_date")
    end_time = data.get("end_time")

    if end_date and end_time:

        payload[AdSet.Field.end_time] = datetime.combine(
            end_date,
            end_time,
        ).isoformat()

    return payload
