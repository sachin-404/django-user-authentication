FROM python:3.12.0a7-buster
WORKDIR /docker-app
COPY requirements.txt /docker-app/
RUN pip install --no-cache-dir -r requirements.txt
COPY . /docker-app/
RUN python manage.py migrate
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]