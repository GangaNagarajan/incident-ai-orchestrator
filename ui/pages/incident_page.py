import streamlit as st

from api_client import APIClient


def incident_page():

    st.title(

        "🚨 New Incident"

    )


    title = st.text_input(

        "Title"

    )


    description = st.text_area(

        "Description"

    )


    application = st.text_input(

        "Application"

    )


    environment = st.selectbox(

        "Environment",

        [

            "development",

            "uat",

            "production"

        ]

    )


    if st.button(

        "Create Incident"

    ):

        payload = {

            "title": title,

            "description": description,

            "application": application,

            "environment": environment

        }


        response = APIClient.create_incident(

            payload

        )


        st.success(

            "Incident Created"

        )


        st.json(

            response

        )


        incident_id = response["incident_id"]


        if st.button(

            "Process Incident"

        ):

            result = APIClient.process_incident(

                incident_id

            )

            st.success(

                "Processing Completed"

            )

            st.json(

                result

            )