# New environment
python3 -m venv sousan-docker
pip install -r ./requirements.txt

# After adding new dependencies
pip freeze > requirements.txt

# Build an image
docker build . -t docker.io/ivanduka/bar:1

# Run an image to use it
docker run --env FILE_ID=4194210 docker.io/ivanduka/bar:1

# During development it's more convenient to BOTH build and run after changes to code:
docker build . -t docker.io/ivanduka/bar:1 && docker run --env FILE_ID=4194210 docker.io/ivanduka/bar:1
