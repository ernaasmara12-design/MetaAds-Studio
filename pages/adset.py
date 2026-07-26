
import streamlit as st

from meta_services.asset_service import AssetService
from components.adset.basic import render_basic

st.set_page_config(
    page_title="Ad Set",
    page_icon="🎯",
)

st.title("🎯 Create Ad Set")

st.caption(
    "Buat Ad Set Meta Ads menggunakan Marketing API"
)

st.divider()

# ==========================
# LOGIN CHECK
# ==========================

if "account_id" not in st.session_state:

    st.error("Silakan login terlebih dahulu.")

    st.stop()

basic = render_basic(
    st.session_state["account_id"]
)

st.divider()
# ==========================
# BUDGET
# ==========================

st.subheader("Budget")

budget_type = st.radio(
    "Budget Type",
    [
        "Daily Budget",
        "Lifetime Budget",
    ],
    horizontal=True,
)

budget = st.number_input(
    "Budget (Rp)",
    min_value=0,
    value=100000,
    step=1000,
)

st.divider()

# ==========================
# SCHEDULE
# ==========================

st.subheader("Schedule")

start_date = st.date_input(
    "Start Date"
)

start_time = st.time_input(
    "Start Time"
)

end_date = st.date_input(
    "End Date"
)

end_time = st.time_input(
    "End Time"
)

st.divider()

# ==========================
# CONVERSION
# ==========================

st.subheader("Conversion")

conversion_location = st.selectbox(
    "Conversion Location",
    [
        "Website",
        "App",
        "Messenger",
        "WhatsApp",
        "Instagram",
    ]
)

performance_goal = st.selectbox(
    "Performance Goal",
    [
        "Maximize Link Clicks",
        "Maximize Landing Page Views",
        "Maximize Conversions",
        "Reach",
    ]
)

pixel = st.selectbox(
    "Meta Pixel",
    [
        "Tidak menggunakan Pixel"
    ]
)

conversion_event = st.selectbox(
    "Conversion Event",
    [
        "PageView",
        "ViewContent",
        "AddToCart",
        "InitiateCheckout",
        "Purchase",
    ]
)

st.divider()

# ==========================
# AUDIENCE
# ==========================

st.subheader("Audience")

country = st.selectbox(
    "Country",
    [
        "Indonesia",
    ]
)

min_age = st.slider(
    "Minimum Age",
    min_value=18,
    max_value=65,
    value=18,
)

max_age = st.slider(
    "Maximum Age",
    min_value=18,
    max_value=65,
    value=65,
)

gender = st.selectbox(
    "Gender",
    [
        "All",
        "Male",
        "Female",
    ]
)

language = st.text_input(
    "Language (Opsional)",
    placeholder="Contoh: Indonesian"
)

interest = st.text_area(
    "Interests",
    placeholder="Contoh: Fashion, Online Shopping, Parenting"
)

st.divider()

st.subheader("Debug")

st.json(
    {
        **basic,

        "budget_type": budget_type,
        "budget": budget,

        "start_date": str(start_date),
        "start_time": str(start_time),

        "end_date": str(end_date),
        "end_time": str(end_time),

        "conversion_location": conversion_location,
        "performance_goal": performance_goal,
        "pixel": pixel,
        "conversion_event": conversion_event,

        "country": country,
        "min_age": min_age,
        "max_age": max_age,
        "gender": gender,
        "language": language,
        "interest": interest,
    }
)
