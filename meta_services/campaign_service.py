"""
Meta Marketing API Campaign Service
"""

from facebook_business.adobjects.adaccount import AdAccount

from meta_payloads.campaign_payload import build_campaign_payload


class CampaignService:

    def __init__(self, account_id: str):
        self.account = AdAccount(account_id)

    def create_campaign(self, data: dict):
        payload = build_campaign_payload(data)

        campaign = self.account.create_campaign(
            params=payload
        )

        return campaign
