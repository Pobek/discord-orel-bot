FROM python:3.8-alpine

WORKDIR /app

COPY . /app

RUN apk add --no-cache gcc musl-dev

RUN pip3 install -r requirements.txt

CMD ["python3", "bot.py"]