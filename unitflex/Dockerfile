
FROM python:3.11-alpine as builder
WORKDIR /app
RUN apk add --no-cache gcc musl-dev libffi-dev

COPY pyproject.toml .
COPY uniflex/ ./uniflex/
COPY cli.py .

RUN pip install --no-cache-dir --prefix=/install requests . && \
    apk del gcc musl-dev libffi-dev

FROM python:3.11-alpine

WORKDIR /app

COPY --from=builder /install /usr/local
COPY uniflex/ ./uniflex/
COPY cli.py .

ENTRYPOINT ["python", "cli.py"]
