FROM python:3.7-alpine
LABEL key="London App Developer Ltd."

#Avoids some complications when running python application
ENV PYTHONUNBUFFERED 1

# Install dependencies
COPY ./requirements.txt /requirements.txt
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
        gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev
RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

# Setup directory structure
RUN mkdir /app
# Sets the default directory
WORKDIR /app
COPY ./app/ /app

# Store any media files
RUN mkdir -p /vol/web/media

# Store any other files such as html, css
RUN mkdir -p /vol/web/static

# We are doing that for security purposes
# -D user that runs applications only
RUN adduser -D user

# The ownership should belong to the user
RUN chown -R user:user /vol/

RUN chmod -R 755 /vol/web

# Swtch to that user
USER user