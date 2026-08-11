import streamlit as st

from pages.incident_page import incident_page
from pages.history_page import history_page
from pages.analytics_page import analytics_page


st.set_page_config(

    page_title="Incident AI Orchestrator",

    page_icon="🤖",

    layout="wide"

)


st.sidebar.title(

    "Incident AI Orchestrator"

)


page = st.sidebar.radio(

    "Navigation",

    [

        "New Incident",

        "Incident History",

        "Analytics"

    ]

)


if page == "New Incident":

    incident_page()

elif page == "Incident History":

    history_page()

else:

    analytics_page()