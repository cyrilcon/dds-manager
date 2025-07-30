FROM python:3.13-slim

WORKDIR /usr/src/app

RUN apt-get update &&  \
    apt-get install -y libpq-dev gcc gettext vim &&  \
    rm -rf /var/lib/apt/lists/*

RUN pip install uv

COPY pyproject.toml uv.lock* ./

RUN uv pip install . --system

COPY . .

CMD ["sh", "-c", "python manage.py migrate && gunicorn dds_manager.wsgi:application --bind 0.0.0.0:8000"]
