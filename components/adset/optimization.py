import streamlit as st


def render_optimization():

    st.subheader("Optimization & Delivery")

    optimization_goal = st.selectbox(
        "Optimization Goal",
        [
            "Link Clicks",
            "Landing Page Views",
            "Conversions",
            "Impressions",
            "Reach",
            "ThruPlay",
            "Post Engagement",
        ],
    )

    billing_event = st.selectbox(
        "Billing Event",
        [
            "Impressions",
            "Clicks",
        ],
    )

    bid_strategy = st.selectbox(
        "Bid Strategy",
        [
            "Highest Volume",
            "Cost Cap",
            "Bid Cap",
            "Minimum ROAS",
        ],
    )

    cost_control = None

    if bid_strategy != "Highest Volume":

        cost_control = st.number_input(
            "Cost Control",
            min_value=0.0,
            step=1.0,
        )

    return {
        "optimization_goal": optimization_goal,
        "billing_event": billing_event,
        "bid_strategy": bid_strategy,
        "cost_control": cost_control,
    }
