# syntax=docker/dockerfile:1
FROM ubuntu:20.04

ADD ./ /waoflix_app
WORKDIR /waoflix_app

RUN DEBIAN_FRONTEND=noninteractive apt update 
RUN DEBIAN_FRONTEND=noninteractive apt install -y python3 python3-pip python3-cairo
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
ENTRYPOINT [ "sh" , "./run_project.sh" ]