from flask import Flask

# !`flask run` will search for app.py and search for variable app. So make sure app.py and app variable are the same name
app = Flask(__name__)

stores = [
    {"name": "My Store", "items": [{"name": "Chair", "price": 15.99}]},
]


# decorator wraps around get_store
@app.get("/store")  # http://127.0.0.1:5000/store
def get_store():
    return {"stores": stores}
