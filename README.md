# fastapi

## Install requeriments

Open git bash an run this command

```bash
pip install psycopg2
```

```bash
pip install -r requirements.txt
```

## Running the application

Complete application is dockerized and docker-compose can be used to run the application.
Environment variables can be configured in config/.env file. config/env.sample provided for reference.
TO simply run the application with default config, you can run the following command.
Application would be available at [http://localhost:9999](http://localhost:9999)

```bash
cd docker && docker compose up
```
