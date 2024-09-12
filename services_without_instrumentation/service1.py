import logging
import time
from fastapi import FastAPI
from elasticapm.contrib.asgi import ElasticAPM

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Elastic APM Configuration
apm = ElasticAPM(app, service_name="FastAPI Service 1", server_url="http://your-apm-server-url", secret_token="your-secret-token")

@app.get("/service1")
async def service1():
    logging.info("Request received by Service 1")
    # Simulate slowness
    time.sleep(2)
    logging.info("Service 1 responding after a delay")
    return {"message": "Hello from Service 1"}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8001)
