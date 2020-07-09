FROM python:latest

RUN mkdir ./app4

COPY . /app4

WORKDIR /app4

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "app.py"]
