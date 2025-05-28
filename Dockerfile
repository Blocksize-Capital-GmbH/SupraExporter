# Base image with Python 3.12
FROM python:3.12-slim

# Set working directory inside the container
WORKDIR /app

# Install Poetry
RUN pip install --no-cache-dir poetry

# Copy only dependency files for layer caching
COPY pyproject.toml poetry.lock* ./

# Install only runtime dependencies (skip dev)
RUN poetry install --no-root --only main

# Copy the actual source code
COPY . .

# Run the supraexporter
CMD ["poetry", "run", "python", "-m", "exporter.main"]
