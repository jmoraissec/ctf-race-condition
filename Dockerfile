FROM python:3.6-slim-buster

COPY . /app
WORKDIR /app

RUN pip install -r requirements.txt

ENV FLAG={Rac3_Th4T_ConD1tiOn}

ENTRYPOINT ["python"]
CMD ["app.py"]
