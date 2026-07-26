from facebook_business.adobjects.adaccount import AdAccount

from meta_payloads.adset_payload import build_adset_payload


class AdSetService:

    def __init__(self, account_id):

        self.account = AdAccount(account_id)

    def create_adset(self, data):

        payload = build_adset_payload(data)

        return self.account.create_ad_set(
            params=payload
        )
