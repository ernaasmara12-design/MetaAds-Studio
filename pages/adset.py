
import streamlit as st

from meta_services.asset_service import AssetService
from components.adset.basic import render_basic
from components.adset.budget import render_budget
from components.adset.schedule import render_schedule
from components.adset.conversion import render_conversion
from components.adset.audience import render_audience

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
budget = render_budget()

st.divider()

schedule = render_schedule()

st.divider()

conversion = render_conversion()

st.divider()

audience = render_audience()

st.divider()

st.subheader("Debug")

st.json(
    {
        **basic,
        **budget,
        **schedule,
        **conversion,
        **audience,
    }
)
