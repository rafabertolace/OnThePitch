FROM python:3.8.6-buster

COPY model.joblib /model.joblib
COPY OnThePitch /OnThePitch
COPY api /api
COPY requirements.txt /requirements.txt
COPY setup.py /setup.py
COPY scripts /scripts

RUN pip install --upgrade pip
RUN pip install -r requirements.txt
#RUN pip install -e .

CMD uvicorn api.api:app --host 0.0.0.0 --port $PORT
