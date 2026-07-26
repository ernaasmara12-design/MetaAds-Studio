import streamlit as st


def render_conversion():

    st.subheader("Conversion")

    conversion_location = st.selectbox(
        "Conversion Location",
        [
            "Website",
            "App",
            "Messenger",
            "WhatsApp",
            "Instagram",
        ],
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
        [
            "PageView",
            "ViewContent",
            "AddToCart",
            "InitiateCheckout",
            "Purchase",
        ],
    )

    return {
        "conversion_location": conversion_location,
        "performance_goal": performance_goal,
        "pixel": pixel,
        "conversion_event": conversion_event,
    }
