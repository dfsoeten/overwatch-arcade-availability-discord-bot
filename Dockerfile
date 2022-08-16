FROM python:3.9-alpine

WORKDIR /src

COPY . .

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3", "-u", "main.py"]