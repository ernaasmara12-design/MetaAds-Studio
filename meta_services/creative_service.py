"""
Meta Marketing API Creative Service
"""

from facebook_business.adobjects.adaccount import AdAccount

from meta_payloads.creative_payload import build_creative_payload


class CreativeService:

    def __init__(self, account_id: str):
        self.account = AdAccount(account_id)

    def create_creative(self, data: dict):
        payload = build_creative_payload(data)

        creative = self.account.create_ad_creative(
            params=payload
        )

        return creative
