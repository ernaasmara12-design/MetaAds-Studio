import json
import streamlit as st


def log_payload(title, payload):

    st.subheader(title)

    st.code(
        json.dumps(
            payload,
            indent=4,
            default=str
        ),
        language="json"
    )
