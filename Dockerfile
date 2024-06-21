# syntax=docker/dockerfile:1
FROM python:3.7-alpine


ADD ./ /waoflix_dj_app
WORKDIR /waoflix_dj_app

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh" , "./run_project.sh" ]