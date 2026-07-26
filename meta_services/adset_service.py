from facebook_business.adobjects.adset import AdSet
from facebook_business.exceptions import FacebookRequestError

from meta_payloads.adset_payload import build_adset_payload
from meta_validators.adset_validator import AdSetValidator
from meta_services.adset_service import AdSetService
from meta_builders.objective_builder import build_objective_defaults


class AdSetService:

    @staticmethod
    def create(account_id, data):

        payload = build_adset_payload(data)

        errors = validate_required_fields(payload)

        if errors:

            raise Exception(
                "\n".join(errors)
            )

        log_payload(
            "Ad Set Payload",
            payload
        )

        adset = AdSet(parent_id=account_id)

        try:

            adset.remote_create(
                params=payload
            )

            return adset

        except FacebookRequestError:

            raise
