import logging
import requests
from fastapi import FastAPI, HTTPException
from elasticapm.contrib.asgi import ElasticAPM

app = FastAPI()

# Set up logging
logging.basicConfig(level=logging.INFO)

# Elastic APM Configuration
apm = ElasticAPM(app, service_name="FastAPI Service 3", server_url="http://your-apm-server-url", secret_token="your-secret-token")

@app.get("/service3")
async def service3():
    logging.info("Request received by Service 3")
    
    # Call Service 2
    try:
        response = requests.get("http://127.0.0.1:8002/service2")
        response.raise_for_status()
        logging.info("Service 3 received response from Service 2")
    except requests.exceptions.RequestException as e:
        logging.error(f"Error calling Service 2: {e}")
        raise HTTPException(status_code=500, detail="Service 2 is unreachable")
    
    return {"message": "Hello from Service 3", "service2_response": response.json()}

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="127.0.0.1", port=8003)
