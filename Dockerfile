FROM python:3.8.10

WORKDIR /usr/src/store


COPY ./requirements.txt ./usr/src/requirements.txt
RUN pip install -r ./usr/src/requirements.txt

RUN rm -rf ./app/botrf
RUN rm -rf ./app/.git
RUN rm -rf ./app/venv

COPY . /usr/src/project

EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]