from facebook_business.adobjects.adset import AdSet


def build_targeting(data):

    targeting = {}

    # Lokasi
    countries = data.get("countries", [])

    if countries:
        targeting["geo_locations"] = {
            "countries": countries
        }

    # Umur
    if data.get("age_min"):
        targeting["age_min"] = data["age_min"]

    if data.get("age_max"):
        targeting["age_max"] = data["age_max"]

    # Gender
    gender = data.get("gender")

    if gender == "Male":
        targeting["genders"] = [1]

    elif gender == "Female":
        targeting["genders"] = [2]

    # Interest
    interests = data.get("interests", [])

    if interests:

        targeting["flexible_spec"] = [
            {
                "interests": interests
            }
        ]

    return {
        AdSet.Field.targeting: targeting
    }
