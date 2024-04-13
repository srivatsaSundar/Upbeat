FROM python:3.11.7-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONBUFFERED 1
ENV APP_ENV prod

WORKDIR /app

COPY . /app

RUN pip install --no-cache-dir -r requiremets.txt

EXPOSE 8080
RUN chmod +x entrypoint.sh
ENTRYPOINT [ "/app/entrypoint.sh" ]