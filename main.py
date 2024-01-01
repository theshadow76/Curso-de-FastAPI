from fastapi import FastAPI

app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

@app.get('/', tags=['Home'])
def message():
    return "Hello World"

@app.get('/test', tags=['Test'])
def test():
    """This is for testing purposes"""
    return "this is a test"