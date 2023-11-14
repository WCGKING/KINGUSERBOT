FROM python:3.10-slim-buster
RUN apt-get update -y
RUN apt-get install git curl python3-pip ffmpeg -y
RUN python3 -m pip install --upgrade pip
RUN pip3 install -U pip
RUN curl -sL https://deb.nodesource.com/setup_18.x | bash -
RUN apt-get install -y nodejs
RUN npm i -g npm
COPY . /Daxx/
WORKDIR /Daxx/
RUN pip3 install -U -r Installer
CMD python3 -m Daxx
