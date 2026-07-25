"""
Meta Marketing API Ad Service
"""

from facebook_business.adobjects.adaccount import AdAccount

from meta_payloads.ad_payload import build_ad_payload


class AdService:

    def __init__(self, account_id: str):
        self.account = AdAccount(account_id)

    def create_ad(self, data: dict):
        payload = build_ad_payload(data)

        ad = self.account.create_ad(
            params=payload
        )

        return ad
