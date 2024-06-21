# syntax=docker/dockerfile:1
FROM ubuntu:22.04

ADD ./ /waoflix_app
WORKDIR /waoflix_app
RUN DEBIAN_FRONTEND=noninteractive apt update
RUN DEBIAN_FRONTEND=noninteractive apt install -y  python3-pip python3-cairo python3-bcrypt python3-requests python3-django python3-gunicorn
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh" , "./run_project.sh" ]