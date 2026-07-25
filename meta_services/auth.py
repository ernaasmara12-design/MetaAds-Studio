"""
Meta Marketing API Authentication
"""

from facebook_business.api import FacebookAdsApi


class MetaAuth:

    def __init__(
        self,
        app_id: str,
        app_secret: str,
        access_token: str,
    ):
        self.app_id = app_id
        self.app_secret = app_secret
        self.access_token = access_token

    def connect(self):
        FacebookAdsApi.init(
            app_id=self.app_id,
            app_secret=self.app_secret,
            access_token=self.access_token,
        )

        return FacebookAdsApi.get_default_api()
