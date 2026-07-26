import streamlit as st

from meta_enums.meta_api_enums import (
    CONVERSION_LOCATIONS,
    CUSTOM_EVENTS,
)


def render_conversion():

    st.subheader("Conversion")

    conversion_location = st.selectbox(
        "Conversion Location",
        list(CONVERSION_LOCATIONS.keys())
    )

    performance_goal = st.selectbox(
        "Performance Goal",
        [
            "Maximize Link Clicks",
            "Maximize Landing Page Views",
            "Maximize Conversions",
            "Reach",
        ],
    )

    pixel = st.selectbox(
        "Meta Pixel",
        [
            "Tidak menggunakan Pixel",
        ],
    )

    conversion_event = st.selectbox(
        "Conversion Event",
        list(CUSTOM_EVENTS.keys())
    )

    return {
        "conversion_location": conversion_location,
        "performance_goal": performance_goal,
        "pixel": pixel,
        "conversion_event": conversion_event,
    }
