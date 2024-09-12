#!/bin/bash

# Start Elastic APM Server (if needed)
# Uncomment and modify the following lines if you need to start Elastic APM Server automatically
# echo "Starting Elastic APM Server..."
# nohup elastic-apm-server > elastic-apm-server.log 2>&1 & echo $! > elastic-apm-server.pid

# Start FastAPI Service 1
echo "Starting FastAPI Service 1..."
nohup python service1.py > service1.log 2>&1 & echo $! > service1.pid

# Start FastAPI Service 2
echo "Starting FastAPI Service 2..."
nohup python service2.py > service2.log 2>&1 & echo $! > service2.pid

# Start FastAPI Service 3
echo "Starting FastAPI Service 3..."
nohup python service3.py > service3.log 2>&1 & echo $! > service3.pid

# Start Prometheus server (if needed)
# echo "Starting Prometheus..."
# nohup prometheus --config.file=prometheus.yml > prometheus.log 2>&1 & echo $! > prometheus.pid

# Start Elasticsearch (if needed)
# echo "Starting Elasticsearch..."
# nohup elasticsearch > elasticsearch.log 2>&1 & echo $! > elasticsearch.pid

# Run the script to fetch metrics and push to Elasticsearch
echo "Running metrics fetch and push script..."
nohup python push_metrics_to_elasticsearch.py > push_metrics_to_elasticsearch.log 2>&1 & echo $! > push_metrics_to_elasticsearch.pid

echo "All services are started."
