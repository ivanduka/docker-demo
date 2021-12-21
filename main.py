from ctypes.util import find_library
import camelot
import os
import ssl
import os
import uuid
from azure.storage.blob import BlobServiceClient, BlobClient, ContainerClient
from dotenv import load_dotenv

# Load environmental variables from .env file if present
load_dotenv()

# Fix bug on MacOS
ssl._create_default_https_context = ssl._create_unverified_context

if __name__ == "__main__":
    azure_key = os.getenv('AZURE_KEY')
    if azure_key == None:
        raise Exception('Must have AZURE_KEY environmental variable to work')


    id = os.getenv('FILE_ID')
    if id == None:
        raise Exception('Must have FILE_ID environmental variable to work')

    
    url = f'https://apps.cer-rec.gc.ca/REGDOCS/File/Download/{id}'
    tables = camelot.read_pdf(url)
    tables.export('foo.csv', f='csv')

    

    print(os.listdir())
    print("Done.")
