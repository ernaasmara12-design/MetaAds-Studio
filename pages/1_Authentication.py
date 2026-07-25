import streamlit as st

from meta_services.auth import MetaAuth

st.set_page_config(page_title="Authentication", page_icon="🔐")

st.title("🔐 Meta Marketing API Authentication")

st.write(
    "Masukkan kredensial Meta Marketing API."
)

app_id = st.text_input("App ID")

app_secret = st.text_input(
    "App Secret",
    type="password"
)

access_token = st.text_area(
    "Access Token",
    height=180
)

if st.button("Connect"):

    try:

        auth = MetaAuth(
            app_id=app_id,
            app_secret=app_secret,
            access_token=access_token,
        )

        api = auth.connect()

        st.session_state["api"] = api
        st.session_state["app_id"] = app_id
        st.session_state["app_secret"] = app_secret
        st.session_state["access_token"] = access_token

        st.success("✅ Connected to Meta Marketing API")

    except Exception as e:
        st.error(str(e))
