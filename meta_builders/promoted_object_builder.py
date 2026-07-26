from facebook_business.adobjects.adset import AdSet

from meta_enums.custom_events import CUSTOM_EVENTS


def build_promoted_object(data):

    promoted_object = {}

    if data.get("conversion_location") == "Website":

        if data.get("pixel_id"):
            promoted_object["pixel_id"] = data["pixel_id"]

        if data.get("conversion_event"):
            promoted_object["custom_event_type"] = CUSTOM_EVENTS[
                data["conversion_event"]
            ]

    if not promoted_object:
        return {}

    return {
        AdSet.Field.promoted_object: promoted_object
    }
