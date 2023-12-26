# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /python-docker

# Copy .env credentials
RUN pip install python-dotenv
COPY .env .
RUN python -c "from dotenv import load_dotenv; load_dotenv('.env')"

# install requirements
COPY webapp/requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip3 install -r requirements.txt

# copy code and data
COPY webapp .
COPY ["model/Luxury watch.csv", "Luxury watch.csv"]

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]