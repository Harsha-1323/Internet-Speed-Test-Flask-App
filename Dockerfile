# Use official Python Image
FROM python:3.11-slim

# Set working directory
WORKDIR /app

# COPY dependencies first
COPY requirements.txt .

# Install dependencies
RUN pip install --no cache-dir -r requirements.txt

# COPY app files
COPY . .

# Expose Flask port
EXPOSE 5000

# Run the app
CMD ["python", "app.py"]
