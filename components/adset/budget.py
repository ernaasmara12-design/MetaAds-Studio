import streamlit as st


def render_budget():

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

    return {
        "budget_type": budget_type,
        "budget": budget,
    }
