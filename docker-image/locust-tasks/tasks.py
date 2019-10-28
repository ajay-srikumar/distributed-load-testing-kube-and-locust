import uuid

from datetime import datetime
from locust import HttpLocust, TaskSet, task


class MetricsTaskSet(TaskSet):
    _deviceid = None

    def on_start(self):
        self._deviceid = str(uuid.uuid4())

    @task
    def login(self):
        self.client.post(
            '/login', {"deviceid": self._deviceid})

    @task
    def post_metrics(self):
        self.client.post(
            "/metrics", {"deviceid": self._deviceid, "timestamp": datetime.now()})


class MetricsLocust(HttpLocust):
    task_set = MetricsTaskSet