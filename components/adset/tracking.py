import streamlit as st


def render_tracking():

    st.subheader("Tracking")

    url_tags = st.text_input(
        "URL Parameters",
        placeholder="utm_source=facebook&utm_medium=cpc",
    )

    tracking = st.checkbox(
        "Enable Meta Tracking",
        value=True,
    )

    return {
        "url_tags": url_tags,
        "tracking": tracking,
    }
