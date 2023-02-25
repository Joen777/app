FROM python:3.9-slim-buster
WORKDIR /test
COPY . .
RUN pip install -r requirements.txt
CMD ["python", "./app.py"]