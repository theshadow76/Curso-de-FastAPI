from fastapi import FastAPI
from fastapi.responses import HTMLResponse

app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

movies = [
    {
        "id" : 1,
        "title" : "movie 1",
        "overview" : "la mejor pelicula del mundo",
        "year" : "2009",
        "rating" : 9.8,
        "category" : "Accion"
    },
    {
        "id" : 2,
        "title" : "movie 1",
        "overview" : "la mejor pelicula del mundo",
        "year" : "2009",
        "rating" : 9.8,
        "category" : "Accion"
    }
]

@app.get('/', tags=['Home'])
def message():
    return HTMLResponse("<h1>Hello! World</h1> \n <p> So proud this works!!! </p>")

@app.get('/test', tags=['Test'])
def test():
    """This is for testing purposes"""
    return "this is a test"

@app.get('/movies', tags=['Movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['Movies'])
def get_movie(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['Movies'])
def get_movies_by_category(category: str):
    return category