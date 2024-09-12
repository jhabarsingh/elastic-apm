#!/bin/bash

# Start Service 1 on port 8001
echo "Starting Service 1 on port 8001..."
uvicorn service1:app --reload --port 8001 &

# Start Service 2 on port 8002
echo "Starting Service 2 on port 8002..."
uvicorn service2:app --reload --port 8002 &

# Start Service 3 on port 8003
echo "Starting Service 3 on port 8003..."
uvicorn service3:app --reload --port 8003 &

# Wait for the background processes to start
wait
