import requests
import streamlit as st


# ============================================================
# CONFIGURATION
# ============================================================

BACKEND_URL = "http://localhost:8000"


# ============================================================
# PAGE CONFIG
# ============================================================

st.set_page_config(
    page_title="Incident AI Orchestrator",
    page_icon="🚨",
    layout="wide"
)


# ============================================================
# HELPER FUNCTIONS
# ============================================================

def get_incidents():

    try:

        response = requests.get(
            f"{BACKEND_URL}/incidents/",
            timeout=10
        )

        if response.status_code == 200:

            return response.json()

        st.error(
            f"Failed to fetch incidents: "
            f"{response.status_code}"
        )

        return []

    except requests.exceptions.RequestException as e:

        st.error(
            f"Unable to connect to backend: {e}"
        )

        return []


def get_analysis(incident_id):

    try:

        response = requests.get(
            f"{BACKEND_URL}/incidents/"
            f"{incident_id}/analysis",
            timeout=10
        )

        if response.status_code == 200:

            return response.json()

        return None

    except requests.exceptions.RequestException:

        return None


def create_incident(
    title,
    description,
    application,
    environment
):

    payload = {
        "title": title,
        "description": description,
        "application": application,
        "environment": environment
    }

    try:

        response = requests.post(
            f"{BACKEND_URL}/incidents/",
            json=payload,
            timeout=10
        )

        if response.status_code in [200, 201]:

            return response.json()

        st.error(
            f"Failed to create incident: "
            f"{response.status_code}"
        )

        st.code(
            response.text
        )

        return None

    except requests.exceptions.RequestException as e:

        st.error(
            f"Unable to connect to backend: {e}"
        )

        return None


def run_ai_analysis(incident_id):

    try:

        response = requests.post(
            f"{BACKEND_URL}/incidents/"
            f"{incident_id}/process",
            timeout=120
        )

        if response.status_code != 200:

            st.error(
                f"AI processing failed: "
                f"{response.status_code}"
            )

            st.code(
                response.text
            )

            return None

        return response.json()

    except requests.exceptions.Timeout:

        st.error(
            "⏱️ AI analysis request timed out."
        )

        return None

    except requests.exceptions.RequestException as e:

        st.error(
            f"Unable to connect to backend: {e}"
        )

        return None


# ============================================================
# HEADER
# ============================================================

st.title(
    "🚨 Incident AI Orchestrator"
)

st.caption(
    "Enterprise Incident Detection, RCA and Resolution"
)


# ============================================================
# CREATE INCIDENT
# ============================================================

st.header(
    "Create New Incident"
)


with st.form(
    "create_incident_form"
):

    col1, col2 = st.columns(2)

    with col1:

        title = st.text_input(
            "Incident Title"
        )

        application = st.text_input(
            "Application"
        )

    with col2:

        environment = st.selectbox(
            "Environment",
            [
                "development",
                "testing",
                "staging",
                "production"
            ]
        )

        description = st.text_area(
            "Incident Description",
            height=120
        )

    create_button = st.form_submit_button(
        "Create Incident"
    )


if create_button:

    if not title:

        st.warning(
            "Please enter an incident title."
        )

    elif not description:

        st.warning(
            "Please enter an incident description."
        )

    elif not application:

        st.warning(
            "Please enter the application."
        )

    else:

        created = create_incident(
            title,
            description,
            application,
            environment
        )

        if created:

            st.success(
                f"Incident created successfully: "
                f"{created.get('incident_id')}"
            )

            st.session_state[
                "selected_incident_id"
            ] = created.get(
                "incident_id"
            )

            st.session_state[
                "latest_analysis"
            ] = None

            st.session_state[
                "analysis_result"
            ] = None

            st.rerun()


# ============================================================
# INCIDENT LIST
# ============================================================

st.divider()

st.header(
    "Existing Incidents"
)


incidents = get_incidents()


if not incidents:

    st.info(
        "No incidents found."
    )

else:

    incident_options = {
        (
            f"{incident.get('incident_id')} - "
            f"{incident.get('title')}"
        ):
            incident.get("incident_id")

        for incident in incidents
    }

    option_labels = list(
        incident_options.keys()
    )

    default_index = 0

    if (
        "selected_incident_id"
        in st.session_state
    ):

        selected_id = st.session_state[
            "selected_incident_id"
        ]

        for index, label in enumerate(
            option_labels
        ):

            if incident_options[label] == selected_id:

                default_index = index

                break

    selected_label = st.selectbox(
        "Select Incident",
        option_labels,
        index=default_index
    )

    selected_incident_id = (
        incident_options[selected_label]
    )

    st.session_state[
        "selected_incident_id"
    ] = selected_incident_id

    selected_incident = next(
        (
            incident
            for incident in incidents
            if incident.get("incident_id")
            == selected_incident_id
        ),
        None
    )


    # ========================================================
    # INCIDENT DETAILS
    # ========================================================

    if selected_incident:

        st.subheader(
            "Incident Details"
        )

        col1, col2, col3 = st.columns(3)

        with col1:

            st.write(
                "**Incident ID:**",
                selected_incident.get(
                    "incident_id"
                )
            )

            st.write(
                "**Title:**",
                selected_incident.get(
                    "title"
                )
            )

        with col2:

            st.write(
                "**Application:**",
                selected_incident.get(
                    "application"
                )
            )

            st.write(
                "**Environment:**",
                selected_incident.get(
                    "environment"
                )
            )

        with col3:

            st.write(
                "**Status:**",
                selected_incident.get(
                    "status"
                )
            )

            st.write(
                "**Priority:**",
                selected_incident.get(
                    "priority"
                )
            )

        st.write(
            "**Description:**"
        )

        st.info(
            selected_incident.get(
                "description",
                ""
            )
        )


    # ========================================================
    # RUN AI ANALYSIS
    # ========================================================

    st.divider()

    st.subheader(
        "AI Analysis"
    )

    if st.button(
        "▶️ Run AI Analysis",
        type="primary"
    ):

        st.session_state[
            "analysis_result"
        ] = None

        with st.spinner(
            "Validating incident..."
        ):

            result = run_ai_analysis(
                selected_incident_id
            )

        if result:

            st.session_state[
                "analysis_result"
            ] = result

            analysis_status = result.get(
                "analysis_status"
            )

            if analysis_status == "REJECTED":

                st.error(
                    "❌ Not an Enterprise IT Incident"
                )

                st.warning(
                    result.get(
                        "rejection_reason",
                        "This request is outside "
                        "enterprise IT incident scope."
                    )
                )

            elif analysis_status == "FAILED":

                st.error(
                    "❌ AI Analysis Failed"
                )

                st.write(
                    result.get(
                        "error",
                        "An unknown error occurred."
                    )
                )

            elif analysis_status == "RUNNING":

                st.success(
                    "✅ Incident AI workflow started."
                )

                st.info(
                    "Click **Refresh Analysis** "
                    "to view the latest result."
                )

            elif analysis_status == "COMPLETED":

                st.success(
                    "✅ AI analysis completed."
                )

            else:

                st.info(
                    result.get(
                        "message",
                        "AI analysis request submitted."
                    )
                )


    # ========================================================
    # REFRESH ANALYSIS
    # ========================================================

    st.divider()

    if st.button(
        "🔄 Refresh Analysis"
    ):

        analysis = get_analysis(
            selected_incident_id
        )

        if analysis:

            st.session_state[
                "latest_analysis"
            ] = analysis

            st.rerun()

        else:

            st.error(
                "Unable to retrieve analysis."
            )


    # ========================================================
    # LOAD EXISTING ANALYSIS
    # ========================================================

    analysis = st.session_state.get(
        "latest_analysis"
    )


    # ========================================================
    # DISPLAY ANALYSIS
    # ========================================================

    if analysis:

        st.divider()

        st.header(
            "Incident Analysis Results"
        )

        analysis_status = analysis.get(
            "analysis_status"
        )

        rejection_reason = analysis.get(
            "rejection_reason"
        )

        analysis_error = analysis.get(
            "analysis_error"
        )


        # ====================================================
        # REJECTED
        # ====================================================

        if analysis_status == "REJECTED":

            st.error(
                "❌ AI Analysis Rejected"
            )

            st.subheader(
                "Reason"
            )

            st.warning(
                rejection_reason
                or
                "This request is outside "
                "enterprise IT incident scope."
            )

            st.info(
                "AI analysis was not started "
                "because this request is not "
                "an enterprise IT incident."
            )


        # ====================================================
        # RUNNING / PENDING
        # ====================================================

        elif analysis_status in [
            "PENDING",
            "RUNNING"
        ]:

            st.info(
                "⏳ AI analysis is still processing..."
            )

            st.write(
                "Please wait and click "
                "**Refresh Analysis**."
            )


        # ====================================================
        # FAILED
        # ====================================================

        elif analysis_status == "FAILED":

            st.error(
                "❌ AI Analysis Failed"
            )

            st.write(
                analysis_error
                or
                "An unknown error occurred "
                "during AI analysis."
            )


        # ====================================================
        # COMPLETED
        # ====================================================

        elif analysis_status == "COMPLETED":

            status = analysis.get(
                "status"
            )

            priority = analysis.get(
                "priority"
            )

            approval_status = analysis.get(
                "approval_status"
            )


            # =================================================
            # STATUS
            # =================================================

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Status",
                    status or "N/A"
                )

            with col2:

                st.metric(
                    "Priority",
                    priority or "N/A"
                )

            with col3:

                st.metric(
                    "Approval",
                    approval_status or "N/A"
                )


            # =================================================
            # ROOT CAUSE
            # =================================================

            st.subheader(
                "🔍 Root Cause"
            )

            root_cause = analysis.get(
                "root_cause"
            )

            if root_cause:

                st.write(
                    root_cause
                )

            else:

                st.info(
                    "Root cause analysis is not available."
                )


            # =================================================
            # CONFIDENCE
            # =================================================

            st.subheader(
                "Confidence"
            )

            confidence = analysis.get(
                "confidence"
            )

            if confidence is not None:

                st.write(
                    confidence
                )

            else:

                st.info(
                    "Confidence is not available."
                )


            # =================================================
            # SUMMARY
            # =================================================

            st.subheader(
                "📝 Summary"
            )

            summary = analysis.get(
                "summary"
            )

            if summary:

                st.write(
                    summary
                )

            else:

                st.info(
                    "Summary is not available."
                )


            # =================================================
            # KNOWLEDGE
            # =================================================

            st.subheader(
                "📚 Knowledge"
            )

            knowledge = analysis.get(
                "knowledge"
            )

            if knowledge:

                if isinstance(
                    knowledge,
                    dict
                ):

                    st.json(
                        knowledge
                    )

                else:

                    st.code(
                        str(knowledge)
                    )

            else:

                st.info(
                    "Knowledge results are not available."
                )


            # =================================================
            # RECOMMENDATIONS
            # =================================================

            st.subheader(
                "💡 Recommendations"
            )

            recommendations = analysis.get(
                "recommendations"
            )

            if recommendations:

                if isinstance(
                    recommendations,
                    dict
                ):

                    st.json(
                        recommendations
                    )

                else:

                    st.code(
                        str(recommendations)
                    )

            else:

                st.info(
                    "Recommendations are not available."
                )


        # ====================================================
        # UNKNOWN STATUS
        # ====================================================

        else:

            st.warning(
                f"Unknown analysis status: "
                f"{analysis_status}"
            )