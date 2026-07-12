import json

from google.cloud import bigquery
from google.oauth2 import service_account

from config import (
    GOOGLE_APPLICATION_CREDENTIALS,
    GOOGLE_SERVICE_ACCOUNT_JSON,
    PROJECT_ID,
)


class BigQueryClient:

    def __init__(self):

        credentials = self._load_credentials()

        self.client = bigquery.Client(
            project=PROJECT_ID,
            credentials=credentials
        )

    def _load_credentials(self):

        if GOOGLE_SERVICE_ACCOUNT_JSON:
            service_account_info = json.loads(GOOGLE_SERVICE_ACCOUNT_JSON)

            return service_account.Credentials.from_service_account_info(
                service_account_info
            )

        return service_account.Credentials.from_service_account_file(
            GOOGLE_APPLICATION_CREDENTIALS
        )

    def execute_query(self, sql: str):

        query_job = self.client.query(sql)

        return query_job.result()
