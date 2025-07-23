FROM python:3.11-slim



WORKDIR /app

# Install dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy app code into container
COPY agent/ agent/

RUN touch agent/__init__.py

# Expose port
EXPOSE 8080

# Start FastAPI using correct module path
CMD ["uvicorn", "agent.main:app", "--host", "0.0.0.0", "--port", "8080"]
