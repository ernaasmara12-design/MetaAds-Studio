"""
Meta Marketing API Asset Service
"""

from facebook_business.adobjects.adaccount import AdAccount


class AssetService:

    def __init__(self, account_id: str):
        self.account = AdAccount(account_id)

    # ==========================
    # Campaigns
    # ==========================

    def get_campaigns(self):

        return self.account.get_campaigns(
            fields=[
                "id",
                "name",
                "status",
                "objective",
            ]
        )

    # ==========================
    # Pixels
    # ==========================

    def get_pixels(self):

        return self.account.get_ads_pixels(
            fields=[
                "id",
                "name",
            ]
        )

    # ==========================
    # Custom Audiences
    # ==========================

    def get_custom_audiences(self):

        return self.account.get_custom_audiences(
            fields=[
                "id",
                "name",
            ]
        )
