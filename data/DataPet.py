category_dict = {
    1: "Dogs",
    2: "Cats",
    3: "Reptiles"
}

status_dict = {
    1: 'available',
    2: 'sold',
    3: 'pending'
}

class DataPet:
    @staticmethod
    def gen_data(pet_id, name, category, photo_urls, tags, status):
        
        pet_json = {
            "id": pet_id,
            "name": name,
            "category": {
                "id": category,
                "name": category_dict[category]
            },
            "photoUrls": photo_urls,
            "tags": tags,
            "status": status_dict[status]
        }
        return pet_json

