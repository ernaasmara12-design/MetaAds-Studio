from facebook_business.adobjects.adset import AdSet
from facebook_business.exceptions import FacebookRequestError

from meta_payloads.adset_payload import build_adset_payload


class AdSetService:

    def __init__(self, account_id):
        self.account_id = account_id

    def create_adset(self, data):

        payload = build_adset_payload(data)

        adset = AdSet(parent_id=self.account_id)

        try:

            adset.remote_create(
                params=payload
            )

            return adset

        except FacebookRequestError as e:
            raise Exception(e.api_error_message())
