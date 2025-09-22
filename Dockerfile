cat > Dockerfile << 'EOF'
# Lightweight Python base image
FROM python:3.12-slim

# Prevent Python from buffering stdout/stderr
ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

# Workdir inside the container
WORKDIR /app

# Install dependencies first (leverages Docker layer caching)
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy the rest of the app
COPY . .

# Flask run settings
ENV FLASK_APP=app.py
ENV FLASK_RUN_HOST=0.0.0.0
# (Optional) ENV FLASK_RUN_PORT=5000

# Expose the dev server port
EXPOSE 5000

# Start the app
CMD ["flask", "run"]
EOF
