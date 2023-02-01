from fastapi import FastAPI, Body
from fastapi.responses import HTMLResponse
from pydantic import BaseModel, Field, Field
from typing import Optional

app = FastAPI()

# cambiar el nombre de la aplicación
app.title = "Mi aplicación con FastAPI"

# cambiar la version de la aplicación
app.version = "0.0.1"

class Movie(BaseModel):
    id: Optional[int] = None
    title: str = Field(min_length=5, max_length=15)
    overview: str = Field(min_length=15, max_length=50)
    year: int = Field(le=2022)
    rating: float = Field(le=10)
    category: str = Field(min_length= 5, max_length=12) 

    class Config:
        schema_extra = {
            "example": {
                "id": 1,
                "title": "Mi pelicula",
                "overview": "Descripcion de la pelicula",
                "year": 2022,
                "rating": 9.8,
                "category": "accion"
            }
        }

movies = [
    {
        'id': 1,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Acción'  
    },
    {
        'id': 2,
        'title': 'Avatar',
        'overview': "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        'year': '2009',
        'rating': 7.8,
        'category': 'Accion'  
    } 
]

# los tags nos permite agrupar las rutas de la aplicación

@app.get('/', tags=['home'])
def message():
    return HTMLResponse("<h1>Hello world!</h1>")


@app.get('/movies', tags=['movies'])
def get_movies():
    return movies

@app.get('/movies/{id}', tags=['movies'])
def get_movies(id: int):
    for item in movies:
        if item["id"] == id:
            return item
    return []

@app.get('/movies/', tags=['movies'])
def get_movies_by_category(category: str, year: int):
    return [item for item in movies if item["category"] == category]

# Metodo create 
@app.post('/movies', tags=['movies'])
def create_movies(movie: Movie):
    movies.append(movie)
    return movies

# Metodo update
@app.put('/movies/{id}', tags=['movies'])
def update_movies(id: int, movie: Movie):
    for item in  movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return movies

# Metodo delete
@app.delete('/movies/{id}', tags=['movies'])
def delete_movies(id: int):
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return movies
