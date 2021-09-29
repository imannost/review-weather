# Dockerfile
FROM python:latest
WORKDIR /review-weather
RUN apt-get update -y
RUN apt-get install -y python3-pip
COPY . .
RUN pip3 install -r requirements.txt
CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]
