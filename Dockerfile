FROM python:3.15.0a8-slim
WORKDIR /app
COPY monitoring.py .
COPY serwery.json .
CMD ["python3", "monitoring.py"]