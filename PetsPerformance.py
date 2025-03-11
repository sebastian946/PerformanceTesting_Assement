from locust import HttpUser,task,between


class PetsStore(HttpUser):
    host = "http://localhost:8080/api/v3"
    wait_time = between(1,5)

    def createPet(self):
        pass