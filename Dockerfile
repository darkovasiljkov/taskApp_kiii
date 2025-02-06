# Use official Python 3.12 base image
FROM python:3.12


WORKDIR /app


COPY . /app


RUN pip install --no-cache-dir -r requirements.txt


EXPOSE 5000


ENV FLASK_APP=run.py
ENV FLASK_ENV=production


CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
