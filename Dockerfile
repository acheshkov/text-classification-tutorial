FROM tiangolo/uwsgi-nginx-flask:python3.6

WORKDIR /app/

COPY requirements.txt /app/
RUN pip install -r ./requirements.txt

ENV ENVIRONMENT production

COPY www/main.py www/__init__.py /app/
COPY model/model.joblib.zip /app/model.joblib.zip
RUN unzip model.joblib.zip