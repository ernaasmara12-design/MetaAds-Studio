"""
Meta Marketing API Asset Service
"""

from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.api import FacebookAdsApi

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
    # Facebook Pages
    # ==========================

    def get_pages(self):
        raise NotImplementedError("get_pages() akan diimplementasikan menggunakan Graph API.")

    # ==========================
    # Instagram Accounts
    # ==========================

    def get_instagram_accounts(self):
        raise NotImplementedError("get_instagram_accounts() akan diimplementasikan menggunakan Graph API.")

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

    # ==========================
    # Saved Audiences
    # ==========================

    def get_saved_audiences(self):
        raise NotImplementedError

    # ==========================
    # Catalogs
    # ==========================

    def get_catalogs(self):
        raise NotImplementedError

    # ==========================
    # Forms
    # ==========================

    def get_forms(self):
        raise NotImplementedError

    # ==========================
    # Images
    # ==========================

    def get_ad_images(self):
        raise NotImplementedError

    # ==========================
    # Videos
    # ==========================

    def get_ad_videos(self):
        raise NotImplementedError
