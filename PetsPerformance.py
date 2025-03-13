from locust import HttpUser, task, between
import json

class PetStoreUser(HttpUser):
    wait_time = between(1, 5)  

    pet_data = {
        "id": 10,
        "name": "Foxy",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "12f"
            }
        ],
        "status": "available"
    }

    updated_pet_data = {
        "id": 10,
        "name": "Max",
        "category": {
            "id": 1,
            "name": "Dogs"
        },
        "photoUrls": ["string"],
        "tags": [
            {
                "id": 0,
                "name": "string"
            }
        ],
        "status": "sold"
    }

    @task
    def create_pet(self):
        
        headers = {
            "accept": "application/xml",
            "Content-Type": "application/json"
        }
        response = self.client.post(
            "/api/v3/pet",
            headers=headers,
            json=self.pet_data
        )
        print(f"Create Pet Response: {response.text}")

    @task
    def find_pets_by_status(self):
        headers = {
            "accept": "application/json"
        }
        response = self.client.get(
            "/api/v3/pet/findByStatus?status=available",
            headers=headers
        )
        print(f"Find Pets by Status Response: {response.text}")

    @task
    def update_pet(self):
        headers = {
            "accept": "application/xml",
            "Content-Type": "application/json"
        }
        response = self.client.put(
            "/api/v3/pet",
            headers=headers,
            json=self.updated_pet_data
        )
        print(f"Update Pet Response: {response.text}")