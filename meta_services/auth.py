"""
Meta Marketing API Authentication
"""

from facebook_business.api import FacebookAdsApi


class MetaAuth:

    @staticmethod
    def connect(
        app_id: str,
        app_secret: str,
        access_token: str,
    ):
        FacebookAdsApi.init(
            app_id=app_id,
            app_secret=app_secret,
            access_token=access_token,
        )

        return True
