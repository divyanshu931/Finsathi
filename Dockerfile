FROM python:3.11-slim

ENV PYTHONDONTWRITEBYTECODE=1 \
    PYTHONUNBUFFERED=1

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

RUN python manage.py collectstatic --noinput

EXPOSE 3000

CMD ["sh", "-c", "python manage.py migrate && gunicorn accounting_project.wsgi:application --bind 0.0.0.0:${PORT:-${APPWRITE_FUNCTION_PORT:-3000}} --workers 2 --timeout 120"]
