from google.cloud import bigquery
from google.oauth2 import service_account

# TODO(developer): Set key_path to the path to the service account key
#                  file.
key_path = "service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

table_id = "backendstarterproject-361103.mydata.inputTable"

# dataset_id = "{}.mydata".format(client.project)

# Construct a full Dataset object to send to the API.
# dataset = bigquery.Dataset(dataset_id)

# TODO(developer): Specify the geographic location where the dataset should reside.
# dataset.location = "US"

# Send the dataset to the API for creation, with an explicit timeout.
# Raises google.api_core.exceptions.Conflict if the Dataset already
# exists within the project.
# dataset = client.create_dataset(dataset, timeout=30)  # Make an API request.
# print("Created dataset {}.{}".format(client.project, dataset.dataset_id))

# schema = [
#         bigquery.SchemaField("input", "STRING", mode="REQUIRED"),
#     ]

# table = bigquery.Table(table_id, schema=schema)
# table = client.create_table(table)  # Make an API request.
# print(
#     "Created table {}.{}.{}".format(table.project, table.dataset_id, table.table_id)
# )