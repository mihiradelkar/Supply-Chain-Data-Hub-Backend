FROM tiangolo/uvicorn-gunicorn-fastapi:python3.8

COPY ./app /app/app
COPY ./requirements.txt /app/requirements.txt
# COPY ./app/data /app/app/data

RUN pip install --no-cache-dir --upgrade -r /app/requirements.txt

EXPOSE 8000

# CMD ["uvicorn", "app.main:app", "--host", "127.0.0.1", "--port", "8000"]
CMD ["uvicorn", "app.main:app", "--host", "0.0.0.0", "--port", "8000"]
