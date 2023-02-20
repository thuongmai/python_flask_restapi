from flask import Flask, request

# !`flask run` will search for app.py and search for variable app. So make sure app.py and app variable are the same name
app = Flask(__name__)

stores = [
    {"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]},
]


# decorator wraps around get_store
@app.get("/store")  # http://127.0.0.1:5000/store
def get_store():
    return {"stores": stores}


@app.post("/store")
def create_store():
    """
    POST: http:/localhost:5000/store
    user_input: {
        "name": "ABC"
    }
    """
    request_data = request.get_json()  # instantiate request to take user input as json
    new_store = {"name": request_data["name"], "item": []}
    stores.append(new_store)
    return new_store, 201  # return tuple of json and code 201:Created


@app.post("store/<string:name>/item")
def create_item(name):
    """
    http://localhost:5000/store/My Store/item
    user_input: {
        'name': 'Table',
        'price': 17.99
    }
    """
    request_data = request.get_json()  # grab incoming json
    for store in stores:
        if store["name"] == name:
            new_item = {"name": request_data["name"], "price": request_data["price"]}
            store["items"].append(new_item)
            return new_item, 201
    return {"message": "Store not found"}, 404
