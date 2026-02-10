#!/bin/bash
PORT=${PORT:-8080}
echo "🚀 Starting Django on port: $PORT"
exec gunicorn sistema_contatos.wsgi:application --bind 0.0.0.0:$PORT
