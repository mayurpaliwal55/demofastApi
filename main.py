from  fastapi import FastAPI
from fastapi.responses import JSONResponse
import service
# Construct a BigQuery client object.
from google.cloud import bigquery
from  fastapi import FastAPI
from fastapi.responses import JSONResponse

from google.cloud import bigquery
from google.oauth2 import service_account

key_path = "service_account.json"

credentials = service_account.Credentials.from_service_account_file(
    key_path, scopes=["https://www.googleapis.com/auth/cloud-platform"],
)

client = bigquery.Client(credentials=credentials, project=credentials.project_id,)

app= FastAPI()

@app.get("/input/{x}")
async def is_valid_input(x:str,status_code=200):
    return service.is_valid_input(x,status_code)

@app.post("/input/{x}")
async def process(x:str):
    sql=f"INSERT mydata.inputTable (input) VALUES('{x}')"

    job = client.query(sql)  # API request.
    job.result()  # Waits for the query to finish.

    print(
        'Created new view "{}.{}.{}".'.format(
            job.destination.project,
            job.destination.dataset_id,
            job.destination.table_id,
        )
    )
    return { "message":"success"}
    
    