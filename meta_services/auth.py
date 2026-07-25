"""
Meta Marketing API Authentication
"""

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount


class MetaAuth:

    @staticmethod
    def connect(
        app_id: str,
        app_secret: str,
        access_token: str,
        account_id: str,
    ):

        FacebookAdsApi.init(
            app_id=app_id,
            app_secret=app_secret,
            access_token=access_token,
        )

        account = AdAccount(account_id)

        account.api_get(
            fields=[
                "id",
                "name",
                "account_status",
            ]
        )

        return True
