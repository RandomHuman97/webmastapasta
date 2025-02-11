FROM python:3.13-alpine

WORKDIR /app

# Install build dependencies
RUN apk update && apk add --no-cache gcc musl-dev linux-headers

# Copy Python dependencies file (create this file with your project dependencies)
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy the application code
COPY main.py .
COPY config.py .


CMD ["python", "main.py"]