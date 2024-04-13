#!/bin/sh

alembic upgrade head 994f5d4ced41

python /app/app.py