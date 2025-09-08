from pymongo import MongoClient

def get_mongo_client(host: str, port: int) -> MongoClient:
    try:
        client = MongoClient(host=host, port=port)
        print(f" Connexion réussie à MongoDB sur {host}:{port}")
        return client
    except Exception as e:
        print(f" Erreur lors de la connexion à MongoDB : {e}")
        return None

if __name__ == "__main__":
    client = get_mongo_client("localhost", 27017)
    if client:
        print("Objet client :", client)



from pymongo import MongoClient

def get_all_laureates(client: MongoClient) -> list[dict]:

    db = client["nobel"]
    collection = db["laureates"]
    laureates = list(collection.find({}, {"_id": 0}))
    return laureates

if __name__ == "__main__":
    def get_mongo_client(host: str, port: int) -> MongoClient:
        return MongoClient(host=host, port=port)

    client = get_mongo_client("localhost", 27017)
    laureates = get_all_laureates(client)
    if laureates:
        print(laureates[-1])
    else:
        print("⚠️ Aucun lauréat trouvé.")


from pymongo import MongoClient

def get_laureates_information(client: MongoClient) -> list[dict]:
    db = client["nobel"]
    collection = db["laureates"]

    laureates = list(collection.find(
        {},
        {"_id": 0, "firstname": 1, "lastname": 1, "born": 1}
    ))
    return laureates

if __name__ == "__main__":
    def get_mongo_client(host: str, port: int) -> MongoClient:
        return MongoClient(host=host, port=port)

    client = get_mongo_client("localhost", 27017)
    laureates = get_laureates_information(client)

    for i in range(2):
        print(laureates[i])


from pymongo import MongoClient

def get_prize_categories(client: MongoClient) -> list[str]:
    db = client["nobel"]
    collection = db["laureates"]

    categories = collection.distinct("category")
    return categories

if __name__ == "__main__":
    def get_mongo_client(host: str, port: int) -> MongoClient:
        return MongoClient(host=host, port=port)

    client = get_mongo_client("localhost", 27017)

    categories = get_prize_categories(client)
    print("Toutes les catégories :", categories)
    laureates = get_laureates_information(client)
    for i in range(2):
        print(laureates[i])




from pymongo import MongoClient

def get_category_laureates(client: MongoClient, category: str) -> list[dict]:
    db = client["nobel"]
    collection = db["laureates"]

    results = collection.find(
        {"category": {"$regex": f"^{category}$", "$options": "i"}},
        {"_id": 0, "firstname": 1, "lastname": 1, "category": 1}
    )

    return list(results)

if __name__ == "__main__":
    def get_mongo_client(host: str, port: int) -> MongoClient:
        return MongoClient(host=host, port=port)

    client = get_mongo_client("localhost", 27017)

    physics_laureates = get_category_laureates(client, "Peace")
    for laureate in physics_laureates[:5]:
        print(laureate)


from pymongo import MongoClient

def get_country_laureates(client: MongoClient, country: str) -> list[dict]:
    db = client["nobel"]
    collection = db["laureates"]

    results = collection.find(
        {"bornCountry": {"$regex": f"^{country}", "$options": "i"}},
        {"_id": 0, "firstname": 1, "lastname": 1, "bornCountry": 1}
    )

    return list(results)

if __name__ == "__main__":
    def get_mongo_client(host: str, port: int) -> MongoClient:
        return MongoClient(host=host, port=port)

    client = get_mongo_client("localhost", 27017)

    french_laureates = get_country_laureates(client, "France")
    for laureate in french_laureates[:5]:
        print(laureate)



def get_shared_prizes(client: MongoClient) -> list[dict]:
    db = client["nobel"]
    collection = db["laureates"]

    pipeline = [
        {"$group": {
            "_id": {"year": "$year", "category": "$category"},
            "laureates": {"$push": {"firstname": "$firstname", "lastname": "$lastname"}},
            "count": {"$sum": 1}
        }},
        {"$match": {"count": {"$gte": 2}}},
        {"$project": {
            "_id": 0,
            "year": "$_id.year",
            "category": "$_id.category",
            "laureates": 1
        }}
    ]

    return list(collection.aggregate(pipeline))


