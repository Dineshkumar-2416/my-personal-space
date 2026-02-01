# Start with Python 3.10 on Linux (slim = smaller size)
FROM python:3.10-slim

# Set working directory inside container
WORKDIR /app

# Copy requirements file first (for better Docker caching)
COPY requirements.txt .

# Install Python packages
RUN pip install --no-cache-dir -r requirements.txt

# Copy all application code
COPY . .

# Document that app uses port 8080
EXPOSE 8080

# Command to run when container starts
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8080"]
