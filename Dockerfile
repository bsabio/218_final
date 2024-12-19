# Start from a base Python image with version 3.10
FROM python:3.10-slim
# Set the working directory
WORKDIR /app
# Copy the current directory contents into the container
COPY . /app
# Set the Python path to /app
ENV PYTHONPATH="/app"
# Install dependencies
RUN pip install -r requirements.txt
# Download wait-for-it script to wait for PostgreSQL before starting FastAPI
RUN apt-get update && apt-get install -y curl && \
    curl -o /usr/local/bin/wait-for-it.sh https://raw.githubusercontent.com/vishnubob/wait-for-it/master/wait-for-it.sh && \
    chmod +x /usr/local/bin/wait-for-it.sh
# Expose the application port
EXPOSE 8000
# Command to start the app, waiting for PostgreSQL before starting FastAPI
CMD ["/usr/local/bin/wait-for-it.sh", "postgres:5432", "--", "uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]