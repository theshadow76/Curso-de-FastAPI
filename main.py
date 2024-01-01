from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title = "Mi app con FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str

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
def get_movies_by_category(category: str, year: int):
    for item in movies:
        if item["category"] == category and item["year"] == year:
            return item
    return []

@app.post('/movies/add', tags=['Movies'])
def create_movie(id: int = Body(), title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    movies.append({
        "id" : id,
        "title" : title,
        "overview" : overview,
        "year" : year,
        "rating" : rating,
        "category" : category
    })
    return movies

@app.put('/movies/edit/{id}', tags=['Movies'])
def update_movie(id: int, title: str = Body(), overview: str = Body(), year: int = Body(), rating: float = Body(), category: str = Body()):
    for item in movies:
        if item['id'] == id:
            item['title'] = title,
            item['overview'] = overview,
            item['year'] = year,
            item['rating'] = rating,
            item['category'] = category
            return movies
    return []

@app.delete('/movies/delete/{id}', tags=['Movies'])
def delete_movie(id: int):
    for item in movies:
        if item['id'] == id:
            movies.remove(item)
            return movies
    return []