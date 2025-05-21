FROM python:3.12-slim
WORKDIR /IT-112
COPY requirements.txt .
RUN pip install -r requirements.txt
CMD ["python", "main.py"]

