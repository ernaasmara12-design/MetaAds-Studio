import streamlit as st


def render_targeting():

    st.subheader("Targeting")

    st.markdown("### Geographic")

    countries = st.multiselect(
        "Countries",
        [
            "Indonesia",
            "Malaysia",
            "Singapore",
            "Thailand",
            "Vietnam",
            "Philippines",
        ],
        default=["Indonesia"],
    )

    cities = st.text_input(
        "Cities (optional)",
        placeholder="Jakarta, Bandung",
    )

    radius = st.number_input(
        "Radius (km)",
        min_value=1,
        value=20,
    )

    return {
        "age_min": age_min,
        "age_max": age_max,
        "gender": gender,
        "languages": languages,
        "countries": countries,
        "cities": cities,
        "radius": radius,
        "interests": interests,
        "excluded_interests": excluded_interests,
        "saved_audience": saved_audience,
        "custom_audience": custom_audience,
        "lookalike": lookalike,
    }

st.divider()

st.markdown("### Custom Audiences")

saved_audience = st.selectbox(
    "Saved Audience",
    [
        "None",
    ],
)

custom_audience = st.selectbox(
    "Custom Audience",
    [
        "None",
    ],
)

lookalike = st.selectbox(
    "Lookalike Audience",
    [
        "None",
    ],
)
  
st.divider()

st.markdown("### Interests")

interests = st.text_area(
    "Interests",
    placeholder="Fashion\nShopee\nParenting",
)

excluded_interests = st.text_area(
    "Exclude Interests",
)

st.divider()

st.markdown("### Demographics")

age_min = st.slider(
    "Minimum Age",
    18,
    65,
    18,
)

age_max = st.slider(
    "Maximum Age",
    18,
    65,
    65,
)

gender = st.selectbox(
    "Gender",
    [
        "All",
        "Male",
        "Female",
    ],
)

languages = st.text_input(
    "Languages",
    placeholder="Indonesian",
)
