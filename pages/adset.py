import streamlit as st

from components.adset.basic import render_basic
from components.adset.budget import render_budget
from components.adset.schedule import render_schedule
from components.adset.conversion import render_conversion
from components.adset.targeting import render_targeting
from components.adset.placement import render_placement
from components.adset.optimization import render_optimization
from components.adset.tracking import render_tracking

from meta_validators.adset_validator import AdSetValidator
from meta_services.adset_service import AdSetService


st.set_page_config(
    page_title="Ad Set",
    page_icon="🎯",
)

st.title("🎯 Create Ad Set")

st.caption(
    "Buat Ad Set Meta Ads menggunakan Marketing API"
)

st.divider()

# ==================================================
# LOGIN CHECK
# ==================================================

if (
    "connected" not in st.session_state
    or not st.session_state["connected"]
):

    st.error("Silakan login terlebih dahulu.")

    st.stop()

# ==================================================
# BASIC
# ==================================================

basic = render_basic(
    st.session_state["account_id"]
)

st.divider()

# ==================================================
# BUDGET
# ==================================================

budget = render_budget()

st.divider()

# ==================================================
# SCHEDULE
# ==================================================

schedule = render_schedule()

st.divider()

# ==================================================
# CONVERSION
# ==================================================

conversion = render_conversion()

st.divider()

# ==================================================
# TARGETING
# ==================================================

targeting = render_targeting()

st.divider()

# ==================================================
# PLACEMENT
# ==================================================

placement = render_placement()

st.divider()

# ==================================================
# OPTIMIZATION
# ==================================================

optimization = render_optimization()

st.divider()

# ==================================================
# TRACKING
# ==================================================

tracking = render_tracking()

st.divider()

# ==================================================
# BUILD DATA
# ==================================================

adset_data = {
    **basic,
    **budget,
    **schedule,
    **conversion,
    **targeting,
    **placement,
    **optimization,
    **tracking,
}

defaults = build_objective_defaults(adset_data)

for key, value in defaults.items():
    if not adset_data.get(key):
        adset_data[key] = value

# ==================================================
# DEBUG
# ==================================================

with st.expander("🐞 Debug Payload", expanded=False):

    st.json(adset_data)

# ==================================================
# CREATE AD SET
# ==================================================

if st.button(
    "🚀 Create Ad Set",
    use_container_width=True,
):

    errors = AdSetValidator.validate(adset_data)

    if errors:

        for error in errors:
            st.error(error)

        st.stop()

    try:

        service = AdSetService(
            account_id=st.session_state["account_id"],
        )

        result = service.create_adset(
            adset_data
        )

        st.success("✅ Ad Set berhasil dibuat.")

        st.code(
            result["id"],
            language="text",
        )

    except Exception as e:

        st.exception(e)
