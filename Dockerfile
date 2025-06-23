# Use official Python image as base
FROM python:3.10-slim

# Set working directory
WORKDIR /app

# Copy requirements and install
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code
COPY . .

# Expose port (matching your app's port)
EXPOSE 8050

# Run app with Gunicorn (production-ready)
CMD ["gunicorn", "--bind", "0.0.0.0:8050", "app:server"]
