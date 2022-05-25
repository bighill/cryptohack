FROM python:3

WORKDIR /solutions

COPY ./solutions/requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY ./solutions .