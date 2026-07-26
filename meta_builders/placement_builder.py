from facebook_business.adobjects.adset import AdSet


def build_placement(data):

    placement = {}

    if data.get("automatic_placement", True):
        return placement

    placement[AdSet.Field.publisher_platforms] = data.get(
        "publisher_platforms",
        ["facebook", "instagram"]
    )

    if data.get("facebook_positions"):
        placement[AdSet.Field.facebook_positions] = data["facebook_positions"]

    if data.get("instagram_positions"):
        placement[AdSet.Field.instagram_positions] = data["instagram_positions"]

    if data.get("messenger_positions"):
        placement[AdSet.Field.messenger_positions] = data["messenger_positions"]

    if data.get("audience_network_positions"):
        placement[
            AdSet.Field.audience_network_positions
        ] = data["audience_network_positions"]

    return placement
