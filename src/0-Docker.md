# Docker Instructions

## Docker Build

```bash
docker build -t hicksm_dev/api -t hicksm_dev/api:0.0 .
```

## Docker Run

```bash
docker run -d -p 8000:8000 \
-e POSTGRES_USER=${POSTGRES_USER} \
-e POSTGRES_PASSWORD=${POSTGRES_PASSWORD} \
-e POSTGRES_ADDRESS=${POSTGRES_ADDRESS} \
-e POSTGRES_DB=${POSTGRES_DB} \
-e SMTP_HOST=${SMTP_HOST} \
-e SMTP_USER=${SMTP_USER} \
-e SMTP_PASS=${SMTP_PASS} \
hicksm_dev/api
```