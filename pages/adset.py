
import streamlit as st

from meta_services.asset_service import AssetService

st.set_page_config(
    page_title="Ad Set",
    page_icon="🎯",
)

st.title("🎯 Create Ad Set")

st.caption(
    "Buat Ad Set Meta Ads menggunakan Marketing API"
)

st.divider()

# ==========================
# LOGIN CHECK
# ==========================

if "account_id" not in st.session_state:

    st.error("Silakan login terlebih dahulu.")

    st.stop()

# ==========================
# LOAD CAMPAIGNS
# ==========================

service = AssetService(
    st.session_state["account_id"]
)

campaign_options = {}

try:

    campaigns = service.get_campaigns()

    for campaign in campaigns:

        campaign_options[
            campaign["name"]
        ] = campaign["id"]

except Exception as e:

    st.error(e)

# ==========================
# BASIC INFORMATION
# ==========================

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

st.divider()

st.subheader("Debug")

st.json(
    {
        "campaign_name": selected_campaign,
        "campaign_id": campaign_options.get(
            selected_campaign
        ),
        "adset_name": adset_name,
        "status": status,
    }
)
