# pull official base image
FROM python:3.11.4-slim-buster

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# set work directory
WORKDIR /app

COPY requirements.txt requirements.txt
RUN pip install -r requirements.txt



# install dependencies
RUN pip install --upgrade pip
#COPY ./requirements.txt .


# copy project
COPY . .
EXPOSE 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
