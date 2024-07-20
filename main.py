from fastapi import FastAPI
import json

app_json = None
with open('./app.json') as file:
    app_json = json.load(file)

app = FastAPI(
    title = app_json["name"],
    version = app_json["version"]
)

@app.get("/config")
async def config():
    data = None
    with open('./config.json') as file:
        data = json.load(file)
    return data
