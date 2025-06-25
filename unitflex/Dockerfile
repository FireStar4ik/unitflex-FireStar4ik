FROM python:3.11-slim

# Set working directory inside container
WORKDIR /app

# Install system dependencies
RUN apt-get update && \
    apt-get install -y curl && \
    rm -rf /var/lib/apt/lists/*

# Install runtime Python dependencies
RUN pip install requests

# Copy everything from unitflex/ into container
COPY . .

# Install package (in editable mode)
RUN pip install -e .

# Set CLI as entrypoint
ENTRYPOINT ["python", "cli.py"]
