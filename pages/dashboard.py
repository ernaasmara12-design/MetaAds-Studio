"""
Dashboard
"""

import streamlit as st

from meta_services.account_service import AccountService

st.set_page_config(
    page_title="Dashboard",
    page_icon="📊",
    layout="wide",
)

st.title("📊 MetaAds Studio Dashboard")

if "meta_api" not in st.session_state:
    st.warning("Silakan login melalui halaman Authentication.")
    st.stop()

account_id = st.session_state["account_id"]

try:

    account = AccountService(account_id)

    info = account.get_account_info()

    st.success("Terhubung ke Meta Marketing API")

    st.subheader("Informasi Akun")

    st.write("**Nama Akun** :", info["name"])
    st.write("**Account ID** :", info["id"])
    st.write("**Status** :", info["account_status"])
    st.write("**Currency** :", info["currency"])
    st.write("**Timezone** :", info["timezone_name"])
    st.write("**Amount Spent** :", info["amount_spent"])

except Exception as e:

    st.error(e)
