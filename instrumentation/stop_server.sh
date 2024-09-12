# Stop FastAPI Service 1
kill $(cat service1.pid)

# Stop FastAPI Service 2
kill $(cat service2.pid)

# Stop FastAPI Service 3
kill $(cat service3.pid)

# Stop Prometheus (if running)
# kill $(cat prometheus.pid)

# Stop Elasticsearch (if running)
# kill $(cat elasticsearch.pid)

# Stop Metrics Fetch and Push Script
kill $(cat push_metrics_to_elasticsearch.pid)
