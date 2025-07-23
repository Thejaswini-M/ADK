from google.cloud import pubsub_v1
import json
import logging

class A2AProtocol:
    def __init__(self, project_id: str, topic_id: str):
        self.publisher = pubsub_v1.PublisherClient()
        self.topic_path = self.publisher.topic_path(project_id, topic_id)

    def send(self, payload: dict):
        message_data = json.dumps(payload).encode("utf-8")
        future = self.publisher.publish(self.topic_path, data=message_data)
        future.result()
        logging.info(f"Published optimization to {self.topic_path}")
