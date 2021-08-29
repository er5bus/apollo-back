FROM python:3.8-slim

LABEL maintainer="Rami sfari <rami2sfari@gmail.com>"

ENV PYTHONPATH=/src
ENV PYTHONUNBUFFERED 1


RUN addgroup --system fastapi \
    && adduser --system --ingroup fastapi fastapi

COPY ./requirements.txt /requirements.txt

RUN pip install --upgrade pip \
    && pip install --no-cache-dir -r /requirements.txt

COPY --chown=fastapi:fastapi src /src

USER fastapi

WORKDIR /src

EXPOSE 80

CMD uvicorn src.main:app --host=0.0.0.0 --port=8080 --log-level=debug --reload --reload-dir=./src --use-colors
