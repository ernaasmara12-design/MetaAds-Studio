from meta_enums.campaign import OBJECTIVES


def build_objective_defaults(data):

    objective = data.get("campaign_objective")

    config = {}

    # Traffic
    if objective == OBJECTIVES["Traffic"]:

        config = {
            "billing_event": "Link Clicks",
            "optimization_goal": "Link Clicks"
        }

    # Awareness
    elif objective == OBJECTIVES["Awareness"]:

        config = {
            "billing_event": "Impressions",
            "optimization_goal": "Reach"
        }

    # Engagement
    elif objective == OBJECTIVES["Engagement"]:

        config = {
            "billing_event": "Impressions",
            "optimization_goal": "Post Engagement"
        }

    # Leads

    elif objective == OBJECTIVES["Leads"]:

        config = {
            "billing_event": "Impressions",
            "optimization_goal": "Conversions"
        }

    # Sales

    elif objective == OBJECTIVES["Sales"]:

        config = {
            "billing_event": "Impressions",
            "optimization_goal": "Conversions"
        }

    # App Promotion

    elif objective == OBJECTIVES["App Promotion"]:

        config = {
            "billing_event": "Impressions",
            "optimization_goal": "ThruPlay"
        }

    return config
