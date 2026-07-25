"""
Meta Marketing API - Creative Payload Builder
"""

from meta_enums.creative import (
    CTA_BUTTONS,
    AD_FORMATS,
)


def build_creative_payload(data: dict) -> dict:
    """
    Build Creative Payload
    """

    payload = {
        "name": data["name"],
        "object_story_spec": {
            "page_id": data["page_id"],
            "link_data": {
                "message": data["primary_text"],
                "link": data["website_url"],
                "name": data["headline"],
                "description": data.get("description", ""),
                "call_to_action": {
                    "type": data["cta"]
                }
            }
        }
    }

    # Optional Image
    if data.get("image_hash"):
        payload["object_story_spec"]["link_data"]["image_hash"] = data["image_hash"]

    # Optional Video
    if data.get("video_id"):
        payload["object_story_spec"]["video_data"] = {
            "video_id": data["video_id"],
            "message": data["primary_text"],
            "title": data["headline"],
        }

    # Optional Instagram Actor
    if data.get("instagram_actor_id"):
        payload["object_story_spec"]["instagram_actor_id"] = data["instagram_actor_id"]

    # Optional URL Tags
    if data.get("url_tags"):
        payload["url_tags"] = data["url_tags"]

    # Optional Tracking Specs
    if data.get("tracking_specs"):
        payload["tracking_specs"] = data["tracking_specs"]

    return payload
