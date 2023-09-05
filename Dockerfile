FROM python:3.8
ENV PYTHONUNBUFFERED 1
ENV PYTHONDONTWRITEBYTECODE 1

# Allows docker to cache installed dependencies between builds
COPY ./requirements.txt requirements.txt
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# Adds our application code to the image
WORKDIR /code
COPY . /code

# Run the production server
CMD newrelic-admin run-program gunicorn --bind 0.0.0.0:8000 --access-logfile - spotify_api.wsgi:application
