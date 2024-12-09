FROM python:3.13-alpine3.19
WORKDIR /app
COPY . /app
RUN apk add --no-cache podman
RUN python3.13 -m pip install -r requirements.txt
RUN ansible-galaxy collection install -r requirements.yml
CMD ["ansible-playbook", "run.yml", "-vv"]
