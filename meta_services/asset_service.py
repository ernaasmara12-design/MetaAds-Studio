"""
Meta Marketing API Asset Service
"""

from facebook_business.adobjects.adaccount import AdAccount


class AssetService:
    """
    Service untuk mengambil seluruh asset Meta Marketing API.
    Seluruh halaman (Campaign, Ad Set, Ads, Dashboard)
    menggunakan service ini.
    """

    def __init__(self, account_id: str):
        self.account = AdAccount(account_id)

    # ==================================================
    # Campaign Assets
    # ==================================================

    def get_campaigns(self):
        return self.account.get_campaigns(
            fields=[
                "id",
                "name",
                "objective",
                "status",
            ]
        )

    # ==================================================
    # Identity Assets
    # ==================================================

    def get_pages(self):
        """
        Akan diimplementasikan menggunakan Graph API.
        """
        raise NotImplementedError(
            "Facebook Pages belum diimplementasikan."
        )

    def get_instagram_accounts(self):
        """
        Akan diimplementasikan menggunakan Graph API.
        """
        raise NotImplementedError(
            "Instagram Accounts belum diimplementasikan."
        )

    # ==================================================
    # Audience Assets
    # ==================================================

    def get_pixels(self):
        return self.account.get_ads_pixels(
            fields=[
                "id",
                "name",
            ]
        )

    def get_custom_audiences(self):
        return self.account.get_custom_audiences(
            fields=[
                "id",
                "name",
            ]
        )

    def get_saved_audiences(self):
        raise NotImplementedError(
            "Saved Audiences belum diimplementasikan."
        )

    # ==================================================
    # Commerce Assets
    # ==================================================

    def get_catalogs(self):
        raise NotImplementedError(
            "Catalogs belum diimplementasikan."
        )

    # ==================================================
    # Lead Assets
    # ==================================================

    def get_forms(self):
        raise NotImplementedError(
            "Lead Forms belum diimplementasikan."
        )

    # ==================================================
    # Creative Assets
    # ==================================================

    def get_ad_images(self):
        raise NotImplementedError(
            "Ad Images belum diimplementasikan."
        )

    def get_ad_videos(self):
        raise NotImplementedError(
            "Ad Videos belum diimplementasikan."
        )
