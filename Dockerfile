FROM python:3.8-slim

WORKDIR /app
COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .

RUN pip install .

ENTRYPOINT ["uvicorn", "asgi:app", "--host", "0.0.0.0"]
CMD ["--port", "8000"]