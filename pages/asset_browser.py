import streamlit as st

from meta_services.asset_service import AssetService

st.set_page_config(
    page_title="Meta Assets",
    page_icon="📂",
)

st.title("📂 Meta Assets")

if "account_id" not in st.session_state:
    st.error("Silakan login terlebih dahulu.")
    st.stop()

service = AssetService(
    st.session_state["account_id"]
)

# ==========================
# Campaigns
# ==========================

st.subheader("Campaigns")

try:

    campaigns = service.get_campaigns()

    rows = []

    for campaign in campaigns:

        rows.append({
            "ID": campaign["id"],
            "Name": campaign["name"],
            "Status": campaign.get("status"),
            "Objective": campaign.get("objective"),
        })

    st.dataframe(rows, use_container_width=True)

except Exception as e:

    st.error(e)

st.divider()

# ==========================
# Pixels
# ==========================

st.subheader("Pixels")

try:

    pixels = service.get_pixels()

    rows = []

    for pixel in pixels:

        rows.append({
            "ID": pixel["id"],
            "Name": pixel["name"],
        })

    st.dataframe(rows, use_container_width=True)

except Exception as e:

    st.error(e)

st.divider()

# ==========================
# Custom Audiences
# ==========================

st.subheader("Custom Audiences")

try:

    audiences = service.get_custom_audiences()

    rows = []

    for audience in audiences:

        rows.append({
            "ID": audience["id"],
            "Name": audience["name"],
        })

    st.dataframe(rows, use_container_width=True)

except Exception as e:

    st.error(e)
