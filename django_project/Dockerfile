FROM python:3.12-slim
WORKDIR /django_assignment
COPY requirements.txt .
RUN pip install -r requirements.txt
# start Django app on port 8000
CMD ["python", "manage.py", "runserver", "0.0.0.0:5000"]