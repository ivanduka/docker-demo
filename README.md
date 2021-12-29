# New environment

- `python3 -m venv docker-demo`
- `pip install -r ./requirements.txt`
- copy `.env.example` to `.env` and fill in the Azure Blob Storage Key

# How to get an Azure Blob Storage Key

- Open https://portal.azure.com
- Create a resource ("+" icon)
- Type "blob" in search bar but do not hit ENTER, choose Storage Account from the dropdown
- Create -> Give it a unique name -> Review + Create -> Create
- Wait until it is created/deployed -> Go to resource
- Access Keys -> Show Keys -> Key 1 -> Copy Connection String
- Paste it into your `.env` file after `AZURE_CONNECTION_STRING=`

# After adding new dependencies you need to save them

- `pip freeze > requirements.txt`

# Build an image

(change `ivanduka` to your username on Docker hub)

- `docker build . -t docker.io/ivanduka/bar:1`

# Run an image to use it

`docker run -env 'FILE_ID=4194210' --env 'AZURE_CONNECTION_STRING=$$$YOUR_SECRET_CONNECTION_STRING$$$' docker.io/ivanduka/bar:1`

# During development it's more convenient to BOTH build and run after changes to code:

(FILE_ID should be dynamically set in production to the target PDF's ID)

- `docker build . -t docker.io/ivanduka/bar:1 ; docker run --env 'FILE_ID=4194210' --env 'AZURE_CONNECTION_STRING=$$$YOUR_SECRET_CONNECTION_STRING$$$' 'docker.io/ivanduka/bar:1'`

# When ready to 'publish' and use by others

- Create a free account on Docker Hub
- Go to your profile, generate a security access token, and save it somewhere safe
- Run `docker login`, and enter your username on Docker Hub and the security token (NOT your password)
- `docker push docker.io/ivanduka/bar:1`
- Now anyone can use your docker container (`docker run...`) over the Internet, including Azure Functions
