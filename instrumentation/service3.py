import time
import random
import elasticapm
from elasticapm.contrib.starlette import ElasticAPM
from prometheus_client import start_http_server, Counter, Histogram
from fastapi import FastAPI, HTTPException

app = FastAPI()

# Configure Elastic APM
app.add_middleware(ElasticAPM, client=elasticapm.Client({
    'SERVICE_NAME': 'service3',
    'SECRET_TOKEN': '',
    'SERVER_URL': 'http://localhost:8200',
}))

# Define Prometheus metrics
REQUESTS = Counter('http_requests_total_service3', 'Total number of HTTP requests for Service 3')
LATENCY = Histogram('http_requests_duration_seconds_service3', 'Duration of HTTP requests for Service 3')

@app.get("/service3")
async def service3():
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
    
    return {"message": "Hello from Service 3"}

if __name__ == "__main__":
    # Start a Prometheus metrics server on port 8006
    start_http_server(8006)
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
