# Use a lightweight Python base image
FROM python:3.13-slim

# Set the working directory
WORKDIR /app

# Copy application files
COPY app.py .

# Install Flask
RUN pip install flask

# Create the content directory
RUN mkdir -p /app/content_store

# Expose the application port
EXPOSE 8080

# Run the application
CMD ["python", "app.py"]
