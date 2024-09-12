import requests
from elasticsearch import Elasticsearch

# Configuration
PROMETHEUS_URL = "http://localhost:9090"
ELASTICSEARCH_URL = "http://localhost:9200"
INDEX_NAME = "prometheus-metrics"
QUERY = "http_requests_total"  # Example query to fetch metrics

def fetch_metrics(prometheus_url, query):
    """
    Fetch metrics from Prometheus.
    """
    response = requests.get(f"{prometheus_url}/api/v1/query", params={"query": query})
    response.raise_for_status()
    return response.json()

def transform_metrics(data):
    """
    Transform Prometheus metrics data to Elasticsearch format.
    """
    metrics = []
    for result in data.get('data', {}).get('result', []):
        metric = result.get('metric', {})
        value = result.get('value', [])[1]
        metrics.append({
            "metric": metric,
            "value": float(value),
        })
    return metrics

def push_to_elasticsearch(elasticsearch_url, index, data):
    """
    Push data to Elasticsearch.
    """
    es = Elasticsearch(elasticsearch_url)
    for metric in data:
        es.index(index=index, body=metric)

if __name__ == "__main__":
    # Fetch metrics from Prometheus
    metrics_data = fetch_metrics(PROMETHEUS_URL, QUERY)
    
    # Transform data
    transformed_data = transform_metrics(metrics_data)
    
    # Push data to Elasticsearch
    push_to_elasticsearch(ELASTICSEARCH_URL, INDEX_NAME, transformed_data)
