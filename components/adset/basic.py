
import streamlit as st

from meta_services.asset_service import AssetService


def render_basic(account_id: str):

    service = AssetService(account_id)

    campaign_options = {}

    try:

        campaigns = service.get_campaigns()

        for campaign in campaigns:

            campaign_options[campaign["name"]] = campaign["id"]

    except Exception as e:

        st.error(e)

    st.subheader("Basic Information")

    adset_name = st.text_input(
        "Ad Set Name",
        placeholder="Contoh : Traffic Indonesia"
    )

    selected_campaign = st.selectbox(
        "Campaign",
        list(campaign_options.keys())
    )

    status = st.selectbox(
        "Status",
        [
            "Active",
            "Paused",
        ]
    )

    return {
        "adset_name": adset_name,
        "campaign_name": selected_campaign,
        "campaign_id": campaign_options.get(selected_campaign),
        "status": status,
    }
