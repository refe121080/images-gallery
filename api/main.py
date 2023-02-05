# save this as app.py
import os
from flask import Flask, request
import requests
from dotenv import load_dotenv
from flask_cors import CORS

load_dotenv(dotenv_path="./.env.local")

UNSPLASH_URL = "https://api.unsplash.com/photos/random"
KEY = os.environ.get("UNSPLASH_KEY", "")
DEBUG = bool(os.environ.get("DEBUG", True))

if not KEY:
    raise EnvironmentError("Please specify the Unsplash API key")

app = Flask(__name__)
CORS(app)

app.config["DEBUG"] = DEBUG


@app.route("/new-image")
def new_image():
    word = request.args.get("query")

    headers = {"Accept-Version": "v1", "Authorization": "Client-ID " + KEY}

    params = {"query": word}

    r = requests.get(url=UNSPLASH_URL, headers=headers, params=params)
    print(r.text)

    return r.json()


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="5050")
