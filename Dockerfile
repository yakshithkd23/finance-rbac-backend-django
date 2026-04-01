FROM python:3.11

WORKDIR /app

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

##------------------- gunicorn for production -------------------------
# EXPOSE 8000
# CMD ["gunicorn","child_nutrition_tracker_backend.wsgi:application", "--bind", "0.0.0.0:8000"]
#------------------------------------------