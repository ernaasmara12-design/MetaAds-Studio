"""
Meta Marketing API Authentication
"""

from facebook_business.api import FacebookAdsApi
from facebook_business.adobjects.adaccount import AdAccount
from facebook_business.adobjects.user import User


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

        user = User(fbid="me")

        user_info = user.api_get(
            fields=[
                "id",
                "name",
            ]
        )

        account = AdAccount(account_id)

        account_info = account.api_get(
            fields=[
                "id",
                "name",
                "currency",
                "timezone_name",
                "account_status",
                "business",
            ]
        )

        return {
            "user": user_info,
            "account": account_info,
            "access_token": access_token,
        }
