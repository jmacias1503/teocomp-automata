FROM python:3.9-alpine

WORKDIR /app

COPY requirements.txt .

RUN pip install --no-cache-dir -r requirements.txt
RUN apk add --no-cache gcc musl-dev linux-headers

COPY . .

CMD ["python", "app/main.py"]
