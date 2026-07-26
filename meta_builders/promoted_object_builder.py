from facebook_business.adobjects.adset import AdSet


def build_promoted_object(data):

    promoted_object = {}

    conversion_location = data.get("conversion_location")

    # Website
    if conversion_location == "Website":

        pixel_id = data.get("pixel_id")

        if pixel_id:
            promoted_object["pixel_id"] = pixel_id

        custom_event = data.get("conversion_event")

        if custom_event:
            promoted_object["custom_event_type"] = custom_event

    # App
    elif conversion_location == "App":

        app_id = data.get("app_id")

        if app_id:
            promoted_object["application_id"] = app_id

    # WhatsApp
    elif conversion_location == "WhatsApp":

        page_id = data.get("page_id")
        whatsapp_number = data.get("whatsapp_number")

        if page_id:
            promoted_object["page_id"] = page_id

        if whatsapp_number:
            promoted_object["whatsapp_phone_number"] = whatsapp_number

    # Messenger
    elif conversion_location == "Messenger":

        page_id = data.get("page_id")

        if page_id:
            promoted_object["page_id"] = page_id

    # Instagram
    elif conversion_location == "Instagram":

        ig_id = data.get("instagram_actor_id")

        if ig_id:
            promoted_object["instagram_actor_id"] = ig_id

    if not promoted_object:
        return {}

    return {
        AdSet.Field.promoted_object: promoted_object
    }
