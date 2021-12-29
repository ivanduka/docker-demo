# New environment

- python3 -m venv docker-demo
- pip install -r ./requirements.txt
- copy `.env.example` to `.env` and fill in the Azure Blob Storage Key

# After adding new dependencies

- pip freeze > requirements.txt

# Build an image

(change `ivanduka` to your username on Docker hub)

- docker build . -t docker.io/ivanduka/bar:1

# Run an image to use it

docker run -env 'FILE_ID=4194210' --env 'AZURE_CONNECTION_STRING=$$$YOUR_SECRET_CONNECTION_STRING$$$' docker.io/ivanduka/bar:1

# During development it's more convenient to BOTH build and run after changes to code:

(FILE_ID should be dynamically set in production to the target PDF's ID)

- docker build . -t docker.io/ivanduka/bar:1 ; docker run --env 'FILE_ID=4194210' --env 'AZURE_CONNECTION_STRING=$$$YOUR_SECRET_CONNECTION_STRING$$$' 'docker.io/ivanduka/bar:1'

# When ready to 'publish' and use by others

- docker push docker.io/ivanduka/bar:1
