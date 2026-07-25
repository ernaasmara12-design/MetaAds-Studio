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

        account_info = MetaAuth.connect(
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

        st.success("✅ Connected to Meta Marketing API")

        st.write("### Account Information")
        st.write(account_info)

    except Exception as e:

        st.session_state["connected"] = False

        st.error(f"❌ Authentication Failed\n\n{e}")
