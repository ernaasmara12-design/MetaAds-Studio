import json

from facebook_business.adobjects.adset import AdSet
from facebook_business.exceptions import FacebookRequestError

from meta_payloads.adset_payload import build_adset_payload


class AdSetService:

    def __init__(self, account_id):
        self.account_id = account_id

    def create_adset(self, data):

        payload = build_adset_payload(data)

        print("=" * 80)
        print("ADSET PAYLOAD")
        print(json.dumps(payload, indent=4, default=str))
        print("=" * 80)

        adset = AdSet(parent_id=self.account_id)

        try:

            adset.remote_create(
                params=payload
            )

            return adset

        except FacebookRequestError as e:

            print("=" * 80)
            print("META API ERROR")
            print(e.body())
            print("=" * 80)

            raise Exception(e.api_error_message())
