FROM python:3.8.0-alpine3.10
LABEL maintainer "ryuichi1208 <ryucrosskey@gmail.com>"

WORKDIR /home/app
COPY . .
RUN apk add --no-cache \
    gcc \
    g++ \
    gfortran \
    make \
    musl \
    && pip install -U pip \
    && pip install -r requirements.txt

ENTRYPOINT ["python", "actions.py"]
