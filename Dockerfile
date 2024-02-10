FROM python:3.10-alpine3.18
LABEL maintainer="samueloliveira.com"

ENV PYTHONUNBUFFERED=1

COPY ./requirements.txt /tmp/requirements.txt
COPY ./app /app
WORKDIR /app
EXPOSE 8000

ARG DEV=false
RUN pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt


# CMD python manage.py runserver

#RUN python -m venv /py && \
#    /py/bin/pip install --upgrade pip && \
#    apk add --update --no-cache --virtual .tmp-build-deps && \
#    /py/bin/pip install -r /tmp/requirements.txt && \
#    rm -rf /tmp && \
#    apk del .tmp-build-deps

