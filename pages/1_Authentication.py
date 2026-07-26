import streamlit as st

from meta_services.auth import MetaAuth

st.set_page_config(
    page_title="Authentication",
    page_icon="🔐",
)

st.title("🔐 Meta Marketing API Authentication")

st.write("Masukkan kredensial Meta Marketing API.")

app_id = st.text_input("App ID")

app_secret = st.text_input(
    "App Secret",
    type="password",
)

access_token = st.text_area(
    "Access Token",
    height=180,
)

account_id = st.text_input(
    "Ad Account ID",
    placeholder="act_1019381049258713",
)

if st.button("Connect"):

    try:

        if not app_id:
            st.error("App ID wajib diisi.")
            st.stop()

        if not app_secret:
            st.error("App Secret wajib diisi.")
            st.stop()

        if not access_token:
            st.error("Access Token wajib diisi.")
            st.stop()

        if not account_id:
            st.error("Ad Account ID wajib diisi.")
            st.stop()

        connection = MetaAuth.connect(
            app_id=app_id,
            app_secret=app_secret,
            access_token=access_token,
            account_id=account_id,
        )

        st.session_state["connected"] = True
        st.session_state["app_id"] = app_id
        st.session_state["app_secret"] = app_secret
        st.session_state["access_token"] = access_token
        st.session_state["account_id"] = account_id
        st.session_state["connection"] = connection
        st.session_state["user"] = connection["user"]
        st.session_state["account"] = connection["account"]
      
        st.success("✅ Connected to Meta Marketing API")

        user = connection["user"]
        account = connection["account"]

        st.divider()

        st.subheader("🟢 Account Information")

        col1, col2 = st.columns(2)

        with col1:
            st.metric(
                "👤 User",
                user["name"]
            )

            st.metric(
                "📢 Ad Account",
                account["name"]
            )

            st.metric(
                "💰 Currency",
                account["currency"]
            )

        with col2:
            st.metric(
                "🆔 Account ID",
                account["id"]
            )

            st.metric(
                "🌍 Timezone",
                account["timezone_name"]
            )

            st.metric(
                "📊 Status",
                str(account["account_status"])
            )

    except Exception as e:

    st.session_state.clear()

    st.error(f"❌ Authentication Failed\n\n{e}")
