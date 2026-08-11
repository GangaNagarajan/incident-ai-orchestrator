import streamlit as st

from api_client import APIClient


def history_page():

    st.title(

        "📄 Incident History"

    )


    incidents = APIClient.get_incidents()


    st.dataframe(

        incidents,

        use_container_width=True

    )