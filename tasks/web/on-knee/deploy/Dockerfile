FROM python:3.10.8

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
EXPOSE 8080

CMD ["uvicorn", "Task8:app", "--host", "0.0.0.0", "--port", "8080"]