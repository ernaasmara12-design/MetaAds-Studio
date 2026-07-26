from datetime import datetime

from facebook_business.adobjects.adset import AdSet


def build_schedule(data):

    payload = {}

    if data.get("start_date") and data.get("start_time"):

        payload[AdSet.Field.start_time] = datetime.combine(
            data["start_date"],
            data["start_time"]
        ).isoformat()

    if data.get("end_date") and data.get("end_time"):

        payload[AdSet.Field.end_time] = datetime.combine(
            data["end_date"],
            data["end_time"]
        ).isoformat()

    return payload
