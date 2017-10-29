FROM python:3.6

RUN apt-get update -y

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

ENV INSTALL_PATH /working_api

RUN mkdir -p $INSTALL_PATH

#Why we need the below:::https://ganesshkumar.com/2016/07/10/docker-disable-python-buffer.html
ENV PYTHONBUFFERED=0

COPY . $INSTALL_PATH

WORKDIR $INSTALL_PATH

CMD ["python", "server.py"]

