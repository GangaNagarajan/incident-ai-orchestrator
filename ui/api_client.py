import requests


BASE_URL = "http://localhost:8000"


class APIClient:


    @staticmethod
    def get_incidents():

        response = requests.get(

            f"{BASE_URL}/incidents/"

        )

        return response.json()


    @staticmethod
    def process_incident(

        incident_id: str

    ):

        response = requests.post(

            f"{BASE_URL}/incidents/{incident_id}/process"

        )

        return response.json()


    @staticmethod
    def create_incident(

        payload: dict

    ):

        response = requests.post(

            f"{BASE_URL}/incidents/",

            json=payload

        )

        return response.json()