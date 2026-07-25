
"""
Dashboard
"""

import streamlit as st

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 MetaAds Studio Dashboard")

if "meta_api" not in st.session_state:

    st.warning(
        "Silakan login terlebih dahulu melalui halaman Authentication."
    )

    st.stop()

st.success("Terhubung ke Meta Marketing API")

st.subheader("Session")

st.write("Ad Account ID:")

st.code(st.session_state["account_id"])
