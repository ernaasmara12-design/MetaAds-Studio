def validate_required_fields(payload):

    required = [

        "name",
        "campaign_id",
        "billing_event",
        "optimization_goal",
        "targeting"

    ]

    errors = []

    for field in required:

        if field not in payload:

            errors.append(
                f"{field} wajib diisi."
            )

    return errors
