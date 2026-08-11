class RCAResponseParser:


    @staticmethod
    def parse(
        response: dict
    ) -> dict:


        if not isinstance(response, dict):

            response = {}


        return {

            "root_cause":
                str(
                    response.get(
                        "root_cause",
                        "Unknown"
                    )
                ),

            "confidence":
                float(
                    response.get(
                        "confidence",
                        0.0
                    )
                ),

            "business_impact":
                str(
                    response.get(
                        "business_impact",
                        ""
                    )
                ),

            "evidence":
                response.get(
                    "evidence",
                    []
                ) or [],

            "immediate_actions":
                response.get(
                    "immediate_actions",
                    []
                ) or [],

            "permanent_actions":
                response.get(
                    "permanent_actions",
                    []
                ) or [],

            "risk":
                str(
                    response.get(
                        "risk",
                        "Unknown"
                    )
                ),

            "affected_component":
                str(
                    response.get(
                        "affected_component",
                        "Unknown"
                    )
                )

        }