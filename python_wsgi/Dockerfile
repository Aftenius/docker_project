FROM python:3.10-slim
WORKDIR /app
COPY requirements.txt .
COPY app.py .
RUN pip install -r requirements.txt
ENV HOST=0.0.0.0
EXPOSE 8082
CMD ["python", "app.py"]