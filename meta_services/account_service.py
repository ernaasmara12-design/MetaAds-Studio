"""
Meta Marketing API Account Service
"""

from facebook_business.adobjects.adaccount import AdAccount


class AccountService:

    def __init__(self, account_id: str):
        self.account = AdAccount(account_id)

    def get_account_info(self):

        fields = [
            "id",
            "name",
            "account_status",
            "currency",
            "timezone_name",
            "amount_spent",
        ]

        return self.account.api_get(fields=fields)
