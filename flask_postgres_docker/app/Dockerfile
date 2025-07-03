FROM python:3.9

WORKDIR /app

COPY . /app

RUN pip install flask flask-sqlalchemy psycopg2-binary

EXPOSE 5000

CMD ["python","-u","app.py"]

