import streamlit as st


def render_audience():

    st.subheader("Audience")

    country = st.selectbox(
        "Country",
        [
            "Indonesia",
        ],
    )

    min_age = st.slider(
        "Minimum Age",
        18,
        65,
        18,
    )

    max_age = st.slider(
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

    language = st.text_input(
        "Language (Optional)",
        placeholder="Contoh: Indonesian",
    )

    interest = st.text_area(
        "Interests",
        placeholder="Fashion, Parenting, Online Shopping",
    )

    return {
        "country": country,
        "min_age": min_age,
        "max_age": max_age,
        "gender": gender,
        "language": language,
        "interest": interest,
    }
