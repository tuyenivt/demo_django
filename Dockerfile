FROM python:3-slim

RUN apt update && apt install -y gcc default-libmysqlclient-dev

WORKDIR /usr/src/app
COPY . /usr/src/app

RUN pip install -r requirements.txt && python manage.py migrate

CMD [ "python", "manage.py", "runserver", "0.0.0.0:8000" ]
