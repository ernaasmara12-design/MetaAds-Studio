from facebook_business.adobjects.adset import AdSet

from meta_enums.meta_api_enums import (
    CONVERSION_LOCATIONS,
    CUSTOM_EVENTS,
)


def build_promoted_object(data):

    promoted_object = {}

    conversion_location = CONVERSION_LOCATIONS.get(
        data.get("conversion_location")
    )

    # ============================================
    # WEBSITE
    # ============================================

    if conversion_location == "WEBSITE":

        pixel_id = data.get("pixel_id")

        if pixel_id:
            promoted_object["pixel_id"] = pixel_id

        event = data.get("conversion_event")

        if event:
            promoted_object["custom_event_type"] = CUSTOM_EVENTS.get(event)

    # ============================================
    # APP
    # ============================================

    elif conversion_location == "APP":

        if data.get("app_id"):
            promoted_object["application_id"] = data["app_id"]

    # ============================================
    # WHATSAPP
    # ============================================

    elif conversion_location == "WHATSAPP":

        if data.get("page_id"):
            promoted_object["page_id"] = data["page_id"]

        if data.get("whatsapp_number"):
            promoted_object["whatsapp_phone_number"] = data["whatsapp_number"]

    # ============================================
    # MESSENGER
    # ============================================

    elif conversion_location == "MESSENGER":

        if data.get("page_id"):
            promoted_object["page_id"] = data["page_id"]

    # ============================================
    # INSTAGRAM
    # ============================================

    elif conversion_location == "INSTAGRAM":

        if data.get("instagram_actor_id"):
            promoted_object["instagram_actor_id"] = data["instagram_actor_id"]

    if not promoted_object:
        return {}

    return {
        AdSet.Field.promoted_object: promoted_object
    }
