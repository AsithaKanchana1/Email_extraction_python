FROM python:3.9-slim

WORKDIR /app

COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

COPY extract_emails.py .

# Optionally, copy a default PDF (or mount it at runtime)
# COPY doc.pdf .

CMD ["python", "extract_emails.py"]
