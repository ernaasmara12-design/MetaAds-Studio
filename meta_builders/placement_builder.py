from facebook_business.adobjects.adset import AdSet
from meta_enums.meta_api_enums import (
    PUBLISHER_PLATFORMS,
)

def build_placement(data):

    placement = {}

    if data.get("automatic_placement", True):
        return placement

    publisher_platforms = data.get("publisher_platforms", [])

if publisher_platforms:
    placement[AdSet.Field.publisher_platforms] = [
        PUBLISHER_PLATFORMS.get(platform, platform)
        for platform in publisher_platforms
    ]

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
