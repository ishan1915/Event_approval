# Use Python 3.10 slim image
FROM python:3.10-slim

# Install required dependencies including PostgreSQL client
RUN apt-get update && \
    apt-get install -y \
    libpq-dev \
    gcc \
    build-essential \
    python3-dev \
    musl-dev \
    pkg-config \
    libmariadb-dev \
    postgresql-client  # Add PostgreSQL client (psql)

# Set the working directory to /app
WORKDIR /app

# Copy requirements file and install dependencies
COPY requirements.txt /app/
RUN pip install --no-cache-dir --upgrade pip && \
    pip install --no-cache-dir -r requirements.txt

# Copy the entire project into the container
COPY . /app/

# Run the application using gunicorn
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
