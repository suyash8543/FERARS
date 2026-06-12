FROM python:3.10-slim

ENV PYTHONUNBUFFERED=1

WORKDIR /app

# System deps needed by some packages (opencv, pillow, etc.)
RUN apt-get update && \
    apt-get install -y --no-install-recommends build-essential libglib2.0-0 libsm6 libxrender1 libxext6 ca-certificates && \
    rm -rf /var/lib/apt/lists/*

# Install Python deps
COPY requirements.txt /app/requirements.txt
RUN pip install --no-cache-dir -r /app/requirements.txt

# Copy project
COPY . /app

# Initialize sqlite DB (seeds recommendations)
RUN python backend/setup_database.py || true

EXPOSE 5000

CMD ["gunicorn", "backend.server:app", "--bind", "0.0.0.0:5000", "--workers", "1", "--timeout", "120"]
