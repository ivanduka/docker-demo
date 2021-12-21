from ctypes.util import find_library
import camelot
import os
import ssl
import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv
import glob

# Load environmental variables from .env file if present
load_dotenv()

# Fix bug on MacOS
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    print("Working...")

    azure_conn_str = os.getenv('AZURE_CONNECTION_STRING')
    if azure_conn_str == None:
        raise Exception(
            'Must have AZURE_CONNECTION_STRING environmental variable to work')

    id = os.getenv('FILE_ID')
    if id == None:
        raise Exception('Must have FILE_ID environmental variable to work')

    url = f'https://apps.cer-rec.gc.ca/REGDOCS/File/Download/{id}'
    tables = camelot.read_pdf(url)
    tables.export('foo.csv', f='csv')

    blob_service_client = BlobServiceClient.from_connection_string(
        azure_conn_str)

    container_name = str(uuid.uuid4())
    blob_service_client.create_container(container_name)
    print(f"Container name: {container_name}")

    files = glob.glob('*.csv')
    for f in files:
        print(f"Uploading {f}")
        with open(f, "rb") as data:
          blob_client = blob_service_client.get_blob_client(container=container_name, blob=os.path.basename(f))
          blob_client.upload_blob(data)

    print("Done.")
