FROM python:3.6.7-jessie

EXPOSE 5000

RUN pip install Flask Flask-Pymongo gunicorn
COPY app.py app.py

CMD ["gunicorn", "-w", "1", "-b", "0.0.0.0:5000", "app:app"]
