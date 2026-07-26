
import streamlit as st

from meta_enums.placement import (
    PLACEMENT_TYPES,
    FACEBOOK_POSITIONS,
    INSTAGRAM_POSITIONS,
    MESSENGER_POSITIONS,
    AUDIENCE_NETWORK_POSITIONS,
    THREADS_POSITIONS,
    DEVICE_TYPES,
    OPERATING_SYSTEMS,
)


def render_placement():

    st.subheader("Placement")

    placement_type = st.radio(
        "Placement Type",
        list(PLACEMENT_TYPES.keys()),
        horizontal=True,
    )

    result = {
        "placement_type": placement_type,
    }

    if placement_type == "Advantage+ Placements":

        st.success(
            "Meta akan menentukan placement terbaik secara otomatis."
        )

        return result

    st.info("Manual Placements")

    # ====================================
    # Facebook
    # ====================================

    with st.expander("Facebook", expanded=True):

        facebook = {}

        for name in FACEBOOK_POSITIONS:

            facebook[name] = st.checkbox(
                name,
                value=True,
                key=f"fb_{name}",
            )

    # ====================================
    # Instagram
    # ====================================

    with st.expander("Instagram", expanded=True):

        instagram = {}

        for name in INSTAGRAM_POSITIONS:

            instagram[name] = st.checkbox(
                name,
                value=True,
                key=f"ig_{name}",
            )

    # ====================================
    # Messenger
    # ====================================

    with st.expander("Messenger"):

        messenger = {}

        for name in MESSENGER_POSITIONS:

            messenger[name] = st.checkbox(
                name,
                value=True,
                key=f"msg_{name}",
            )

    # ====================================
    # Audience Network
    # ====================================

    with st.expander("Audience Network"):

        audience_network = {}

        for name in AUDIENCE_NETWORK_POSITIONS:

            audience_network[name] = st.checkbox(
                name,
                value=True,
                key=f"an_{name}",
            )

    # ====================================
    # Threads
    # ====================================

    with st.expander("Threads"):

        threads = {}

        for name in THREADS_POSITIONS:

            threads[name] = st.checkbox(
                name,
                value=True,
                key=f"th_{name}",
            )

    st.divider()

    devices = st.multiselect(
        "Devices",
        list(DEVICE_TYPES.keys()),
        default=list(DEVICE_TYPES.keys()),
    )

    operating_systems = st.multiselect(
        "Operating Systems",
        list(OPERATING_SYSTEMS.keys()),
        default=list(OPERATING_SYSTEMS.keys()),
    )

    result.update({
        "facebook": facebook,
        "instagram": instagram,
        "messenger": messenger,
        "audience_network": audience_network,
        "threads": threads,
        "devices": devices,
        "operating_systems": operating_systems,
    })

    return result
