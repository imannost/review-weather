# Dockerfile
FROM python:3.8.10
WORKDIR /review-weather
RUN apt-get update -y
RUN apt-get install -y python3-pip
COPY requirements.txt .
RUN pip3 install -r requirements.txt
COPY . .
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
