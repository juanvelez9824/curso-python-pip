from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel
from typing import Optional

app = FastAPI()
app.title="Mi aplicacion con FastAPI"
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str
    overview: str
    year: int
    rating: float
    category: str


movies = [{
    "id":1,
    "title":"Avatar",
    "overview":"en un exuberante planeta llamado pandora viven lo na´vi",
    "year": "2009",
    "rating":7.8,
    "category":"Accion"
}
]
@app.get("/",tags=["Home"])

def message():
    return HTMLResponse("<h1>hello world </h1>")

@app.get("/movies", tags=["movies"])
def get_movies():
    return movies


@app.get("/movies/{id}" ,tags=["movies"])
def get_movies(id:int):
    for item in movies:
        if item["id"]==id:
            return item
    return []
@app.get("/movies/",tags=["movies"])
def get_movies_by_category(category:str,year:int):
    return [ item for item in movies if item["category"] == category]


@app.post("/movies",tags=["movies"])
def create_movie(movie : Movie):
    movies.append(movie)
    return movies


@app.put("/movies/{id}", tags=["movies"])
def update_movie(id:int, movie:Movie):
    for item in movies:
         if item["id"]==id:
             item["title"]= movie.title
             item["overview"]=movie.overview
             item["year"] = movie.year
             item["rating"] = movie.rating
             item["category"] = movie.category
             return movies


@app.delete("/movies/{id}",tags=["movies"])
def delete_movies(id: int):
    for item in movies:
         if item["id"]==id:
             movies.remove(item)
             return movies
             



             

       
