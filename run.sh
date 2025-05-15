#!/bin/bash
docker-compose down
docker-compose build
docker-compose up -d
sleep 3
curl http://localhost:8000/docs