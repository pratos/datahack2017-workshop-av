#Base Image
FROM python:3.6

#Update the system
RUN apt-get update -y

#Copy the requirements.txt file
COPY requirements.txt requirements.txt

#pip install
RUN pip install --no-cache-dir -r requirements.txt

#Assigning environment variable
ENV INSTALL_PATH /working_api

#Create the installation path
RUN mkdir -p $INSTALL_PATH

#Why we need the below:::https://ganesshkumar.com/2016/07/10/docker-disable-python-buffer.html
ENV PYTHONBUFFERED=0

#Copy all the content
COPY . $INSTALL_PATH

WORKDIR $INSTALL_PATH

#Command run on local system
CMD ["python", "server.py"]


