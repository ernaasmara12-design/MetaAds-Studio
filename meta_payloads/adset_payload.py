from facebook_business.adobjects.adset import AdSet

from meta_builders.budget_builder import build_budget
from meta_builders.optimization_builder import build_optimization
from meta_builders.schedule_builder import build_schedule


def build_adset_payload(data):

    payload = {

        AdSet.Field.name: data["adset_name"],

        AdSet.Field.campaign_id: data["campaign_id"],

        AdSet.Field.status: "PAUSED",

    }

    payload.update(build_budget(data))
    payload.update(build_optimization(data))
    payload.update(build_schedule(data))

    return payload
