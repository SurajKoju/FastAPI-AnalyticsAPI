# Analytics API using FastAPI + Time-series Postgres

Building an Analytics API service with Python, FastAPI, and Time-series Postgres with TimescaleDB

## Docker
- `docker build -t analytics-api -f Dockerfile.web .`
- `docker run analytics-api `
- Docker compose is for the local development purpose and docker-run.sh is for the production level and to distinguish the production and the local the code is written in the Dockerfile. `CMD ["/opt/run.sh"]`