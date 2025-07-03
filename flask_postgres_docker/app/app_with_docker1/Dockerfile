# Use official Python image
FROM python:3.9

# Set environment variables
ENV POSTGRES_USER=postgres
ENV POSTGRES_PASSWORD=password
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_HOST=postgres_container  
# Use the PostgreSQL container name
ENV POSTGRES_PORT=5432

# Set working directory
WORKDIR /app

# Copy application files
COPY .  /app

# Install dependencies
RUN pip install flask flask-sqlalchemy psycopg2-binary

# Expose Flask port
EXPOSE 5000

# Run the Flask application
CMD ["python", "-u", "app.py"]

