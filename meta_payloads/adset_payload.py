from facebook_business.adobjects.adset import AdSet

from meta_enums.meta_api_enums import ADSET_STATUS

from meta_builders.budget_builder import build_budget
from meta_builders.optimization_builder import build_optimization
from meta_builders.schedule_builder import build_schedule
from meta_builders.targeting_builder import build_targeting
from meta_builders.placement_builder import build_placement
from meta_builders.promoted_object_builder import build_promoted_object


def build_adset_payload(data):

    payload = {
        AdSet.Field.name: data.get("adset_name"),
        AdSet.Field.campaign_id: data.get("campaign_id"),
        AdSet.Field.status: ADSET_STATUS["Paused"],
    }

    payload.update(build_budget(data))
    payload.update(build_schedule(data))
    payload.update(build_optimization(data))
    payload.update(build_targeting(data))
    payload.update(build_placement(data))
    payload.update(build_promoted_object(data))

    return payload
