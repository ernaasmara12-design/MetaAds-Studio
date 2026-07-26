import streamlit as st


def render_schedule():

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

    return {
        "start_date": start_date,
        "start_time": start_time,
        "end_date": end_date,
        "end_time": end_time,
    }
