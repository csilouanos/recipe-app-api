FROM python:3.7-alpine
LABEL key="London App Developer Ltd."

#Avoids some complications when running python application
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
# Sets the default directory
WORKDIR /app
COPY ./app/ /app

# We are doing that for security purposes
# -D user that runs applications only
RUN adduser -D user
# Swtch to that user
USER user