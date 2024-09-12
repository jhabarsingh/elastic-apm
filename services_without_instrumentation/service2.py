import logging
import time
import requests
from fastapi import FastAPI, HTTPException
from elasticapm.contrib.asgi import ElasticAPM

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Elastic APM Configuration
apm = ElasticAPM(app, service_name="FastAPI Service 2", server_url="http://your-apm-server-url", secret_token="your-secret-token")

@app.get("/service2")
async def service2():
    logging.info("Request received by Service 2")
    
    # Call Service 1
    try:
        response = requests.get("http://127.0.0.1:8001/service1")
        response.raise_for_status()
        logging.info("Service 2 received response from Service 1")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling Service 1: {e}")
        raise HTTPException(status_code=500, detail="Service 1 is unreachable")

    # Simulate slowness
    time.sleep(1)
    logging.info("Service 2 responding after delay")
    
    return {"message": "Hello from Service 2", "service1_response": response.json()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8002)
