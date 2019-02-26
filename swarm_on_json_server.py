from locust import HttpLocust, TaskSet, task

class UserBehaviour(TaskSet):
    @task(3)
    def profile(self):
        self.client.get("/profile")

    @task(2)
    def posts(self):
        response = self.client.post("/posts",  {"title": "new post","author": "Scale"})
        new_post_id = response.json()['id']
        self.client.delete("/posts/" + str(new_post_id))
        self.client.get("/posts")

    @task(1)
    def comments(self):
        self.client.post("/comments",  {"body": "new comment","postId": 1})
        self.client.get("/comments")

class WebsiteUser(HttpLocust):
    task_set = UserBehaviour
    min_wait = 5000
    max_wait = 9000