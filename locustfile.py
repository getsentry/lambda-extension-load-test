from locust import HttpUser, constant, task


class WebsiteUser(HttpUser):
    wait_time = constant(1)

    @task
    def home(self):
        self.client.get("/api")

    @task
    def ok(self):
        self.client.get("/api/boom")

    @task
    def boom(self):
        self.client.get(f"/api/boom?trigger=1")

    @task
    def zero(self):
        self.client.get(f"/api/zero")
