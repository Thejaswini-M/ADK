from fastapi import FastAPI
from models import InputData
from agent_class import OptimizationAgent
from a2a_messenger import A2AProtocol
import logging
import os
import uvicorn

app = FastAPI()
logging.basicConfig(level=logging.INFO)
# mocked gcp id
PROJECT_ID = "gcp_project_id"
# mocked pubsub topic
TOPIC_ID = "optimization-suggestion-topic"

agent = OptimizationAgent()
messenger = A2AProtocol(PROJECT_ID, TOPIC_ID)

@app.post("/a2a/lca")
def receive_lca(data: InputData):
    logging.info(f"Received data : {data}")
    suggestion = agent.process(data)
    logging.info(f"Generated suggestion: {suggestion}")
    messenger.send(suggestion.dict())
    return {"status": "suggestion published", "suggestion": suggestion}

