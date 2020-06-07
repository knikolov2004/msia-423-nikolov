#!/usr/bin/env bash

python3 ingestion.py create_db
python3 ingestion.py ingest
python3 app.py