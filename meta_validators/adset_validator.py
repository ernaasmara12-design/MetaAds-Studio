
class AdSetValidator:

    @staticmethod
    def validate(data):

        errors = []

        if not data.get("adset_name"):
            errors.append("Ad Set Name wajib diisi.")

        if not data.get("campaign_id"):
            errors.append("Campaign harus dipilih.")

        if data.get("budget", 0) <= 0:
            errors.append("Budget harus lebih besar dari 0.")

        if data.get("min_age") > data.get("max_age"):
            errors.append("Minimum age tidak boleh lebih besar dari maximum age.")

        return errors
