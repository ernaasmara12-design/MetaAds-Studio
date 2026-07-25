import streamlit as st

st.set_page_config(
    page_title="Campaign",
    page_icon="📢",
)

st.title("📢 Create Campaign")

st.caption(
    "Buat Campaign Meta Ads menggunakan Marketing API"
)

st.divider()

st.subheader("Basic Campaign Information")

campaign_name = st.text_input(
    "Campaign Name",
    placeholder="Contoh: Summer Sale 2026"
)

objective = st.selectbox(
    "Campaign Objective",
    [
        "Awareness",
        "Traffic",
        "Engagement",
        "Leads",
        "App Promotion",
        "Sales",
    ]
)

buying_type = st.selectbox(
    "Buying Type",
    [
        "AUCTION",
    ]
)

campaign_status = st.selectbox(
    "Campaign Status",
    [
        "ACTIVE",
        "PAUSED",
    ]
)

st.divider()

st.info(
    "Tahap berikutnya kita akan menambahkan pengaturan Budget."
)
