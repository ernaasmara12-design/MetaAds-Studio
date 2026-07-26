class AdSetValidator:

    @staticmethod
    def validate(data):

        errors = []

        # ==========================
        # Basic
        # ==========================

        if not data.get("adset_name"):
            errors.append("Ad Set Name wajib diisi.")

        if not data.get("campaign_id"):
            errors.append("Campaign harus dipilih.")

        # ==========================
        # Budget
        # ==========================

        budget = data.get("budget", 0)

        if budget <= 0:
            errors.append("Budget harus lebih besar dari 0.")

        # ==========================
        # Targeting
        # ==========================

        age_min = data.get("age_min")
        age_max = data.get("age_max")

        if (
            age_min is not None
            and age_max is not None
            and age_min > age_max
        ):
            errors.append(
                "Minimum age tidak boleh lebih besar dari maximum age."
            )

        return errors
