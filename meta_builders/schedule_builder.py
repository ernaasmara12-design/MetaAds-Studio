from datetime import datetime

from facebook_business.adobjects.adset import AdSet


def build_schedule(data):

    payload = {}

    start_date = data.get("start_date")
    start_time = data.get("start_time")

    if start_date and start_time:
        payload[AdSet.Field.start_time] = datetime.combine(
            start_date,
            start_time
        ).isoformat()

    end_date = data.get("end_date")
    end_time = data.get("end_time")

    if end_date and end_time:
        payload[AdSet.Field.end_time] = datetime.combine(
            end_date,
            end_time
        ).isoformat()

    return payload
