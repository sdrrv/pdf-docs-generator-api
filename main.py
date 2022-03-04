from fastapi import FastAPI, Query
from typing import List, Optional

app = FastAPI()

@app.get("/")
def index():
    return{
        "NAME": "pdf-docs-generator-api",
        "AUTHOR": "Duarte Elvas",
        "VERSION": "0.0.1",
        "AUTHOR_PORTFOLIO":"https://web.tecnico.ulisboa.pt/duartecelvas"
    }

#@app.get("/")