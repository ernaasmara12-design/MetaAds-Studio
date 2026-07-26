
import streamlit as st

from components.adset.basic import render_basic
from components.adset.budget import render_budget
from components.adset.schedule import render_schedule
from components.adset.conversion import render_conversion
from components.adset.targeting import render_targeting
from components.adset.placement import render_placement
from components.adset.optimization import render_optimization
from components.adset.tracking import render_tracking

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

targeting = render_targeting()

st.divider()

placement = render_placement()

st.divider()

optimization = render_optimization()

st.divider()

tracking = render_tracking()

st.divider()

st.subheader("Debug")

st.json(
    {
        **basic,
        **budget,
        **schedule,
        **conversion,
        **targeting,
        **placement,
        **optimization,
        **tracking,
    }
)

from meta_validators.adset_validator import AdSetValidator
from meta_services.adset_service import AdSetService

if st.button(
    "🚀 Create Ad Set",
    use_container_width=True,
):

    adset_data = {
        **basic,
        **budget,
        **schedule,
        **conversion,
        **audience,
        **placement,
        **optimization,
        **tracking,
    }

    errors = AdSetValidator.validate(adset_data)

    if errors:

        for error in errors:
            st.error(error)

    else:

        service = AdSetService(
            st.session_state["account_id"]
        )

        try:

            result = service.create_adset(
                adset_data
            )

            st.success(
                f"Ad Set berhasil dibuat.\n\nID: {result['id']}"
            )

        except Exception as e:

            st.exception(e)
