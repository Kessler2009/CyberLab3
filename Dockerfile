FROM python:3.9-alpine

COPY ./requirements.txt /app/requirements.txt


ENV STATIC_URL /static
ENV STATIC_PATH /Cyber1/static

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
ADD . .
COPY . .

CMD [ "python3", "main.py"]