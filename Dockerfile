FROM python:3.12.4-slim-bookworm
WORKDIR /app
COPY requirements ./
RUN pip3 install -r requirements
COPY . .
EXPOSE 8000
CMD [ "uvicorn", "main:app", "--port=8000", "--host=0.0.0.0" ]
