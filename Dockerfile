FROM python:3
ENV PYTHONUNBUFFERED 1
COPY . /srv/FDM
WORKDIR /srv/FDM
RUN pip install -r /srv/FDM/requirements/dev.txt

