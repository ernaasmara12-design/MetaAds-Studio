"""
Authentication Page
"""

import streamlit as st

from meta_services.auth import MetaAuth


st.set_page_config(
    page_title="Authentication",
    page_icon="🔐",
    layout="wide",
)

st.title("🔐 Meta Marketing API Authentication")

st.write(
    "Masukkan kredensial Meta Marketing API untuk menghubungkan aplikasi."
)

app_id = st.text_input("App ID")
app_secret = st.text_input("App Secret", type="password")
access_token = st.text_area("Access Token", height=150)
account_id = st.text_input(
    "Ad Account ID",
    placeholder="act_1234567890"
)

if st.button("Connect to Meta API"):

    if not app_id:
        st.error("App ID wajib diisi")
        st.stop()

    if not app_secret:
        st.error("App Secret wajib diisi")
        st.stop()

    if not access_token:
        st.error("Access Token wajib diisi")
        st.stop()

    if not account_id:
        st.error("Ad Account ID wajib diisi")
        st.stop()

    try:

        auth = MetaAuth(
            app_id=app_id,
            app_secret=app_secret,
            access_token=access_token,
        )

        api = auth.connect()

        st.session_state["meta_api"] = api
        st.session_state["account_id"] = account_id

        st.success("Berhasil terhubung ke Meta Marketing API")

    except Exception as e:
        st.error(str(e))
