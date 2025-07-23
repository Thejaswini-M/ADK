LCA Optimization Agent (FastAPI + GCP Pub/Sub)

This project implements a lightweight  Optimization Agent as a REST API using FAST API, simulating an ADK-style agent. 
It receives LCA data, applies simple optimization logic, and publishes optimization suggestions to a Google Cloud Pub/Sub topic for downstream consumption (by another agent  HiL Agent).

Features & Flow:
-->A http endpoint to receive a lca crate data and processing logic to produce otimized suggestion 
-->Publishing the optimized suggestion to a optimized pubsub topic
-->The message is consumed by the subscriber of optimized pubsub topic (HIL agent)

Folder Structure

── Dockerfile # Dockerfile for containerizing the agent
├── requirements.txt # Python dependencies
├── README.md
└── agent/
  ├── main.py # FastAPI entrypoint
  ├── models.py # Pydantic data models
  ├── lca_agent.py # Core logic for LCA processing
  └── a2a_messenger.py # Publishes messages to Pub/Sub

  **Assuming the hil agent which is a another cloud run service is a subscriber to the optimized pubsub topic.

**  Deploy Instructions **
steps
-->Create a cloud pub/sub topic on name optimization-suggestion-topic and make hil agent  service as a subscriber.
-->Create a cloudbuild.yaml which  consists the step  to build  image and deploy container to cloud run as a service.
-->create cloud build trigger  by mapping guthub source and  cloudbuild yaml as reference
Test:
-->perform a commit in github and observe or monitor the build in cloud build.



