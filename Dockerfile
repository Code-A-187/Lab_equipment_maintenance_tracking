FROM python:3.13

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt

# Create non-root user
RUN useradd app

# Copy files AND assign ownership directly to 'app' user
COPY --chown=app:app main.py .
COPY --chown=app:app app.py .
COPY --chown=app:app lab.db .

USER app

EXPOSE 8000


CMD ["uvicorn", "main:app", "--host", "0.0.0.0", "--port", "8000"]

