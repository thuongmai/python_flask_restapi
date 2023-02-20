# Simple GET method using flask
## Installation
`pip install flask`
## Run the program
Create a `app.py` file and add this:
```python
from flask import Flask
app = Flask(__name__)
```
Then run command:
`flask run`
So what this command does is looking for a default file called `app.py`, and looking for a variable name `app`
We have nothing declared so it should return 404
## Adding GET method
```python
# decorator wraps around get_store
@app.get("/store")  # http://127.0.0.1:5000/store
def get_store():
    return {"stores": stores}
```
We add a function with a wrap decorator called `@app.get('/store')` to tell RESTapi the path and this function will return value at `http://localhost:5000/store`