from fastapi import FastAPI

@app.get('/')
def home():
    return{"Hello":"World"}
