import time
import random
import elasticapm
from elasticapm.contrib.starlette import ElasticAPM
from prometheus_client import start_http_server, Counter, Histogram
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Configure Elastic APM
app.add_middleware(ElasticAPM, client=elasticapm.Client({
    'SERVICE_NAME': 'service1',
    'SECRET_TOKEN': '',
    'SERVER_URL': 'http://localhost:8200',
}))

# Define Prometheus metrics
REQUESTS = Counter('http_requests_total_service1', 'Total number of HTTP requests for Service 1')
LATENCY = Histogram('http_requests_duration_seconds_service1', 'Duration of HTTP requests for Service 1')

@app.get("/service1")
async def service1():
    start_time = time.time()
    REQUESTS.inc()
    
    # Simulate a slow request
    delay = random.uniform(0, 2)
    time.sleep(delay)
    
    # Simulate an error
    if random.random() < 0.1:
        raise HTTPException(status_code=500, detail="Internal Server Error")
    
    duration = time.time() - start_time
    LATENCY.observe(duration)
    
    return {"message": "Hello from Service 1"}

if __name__ == "__main__":
    # Start a Prometheus metrics server on port 8004
    start_http_server(8004)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
