from fastapi import FastAPI, Body, Path, Query
from fastapi.responses import HTMLResponse, JSONResponse
from pydantic import BaseModel, Field, Field
from typing import Optional, List

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
    rating: float = Field(ge=1,le=10)
    category: str = Field(min_length= 5, max_length=12) 
# ge = mayor o igual a || le = menor o igual
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


@app.get('/movies', tags=['movies'], response_model=List[Movie])
def get_movies() -> List[Movie]:
    return JSONResponse(content=movies)

@app.get('/movies/{id}', tags=['movies'], response_model=Movie)
def get_movies(id: int = Path(ge=1, le=2000)) -> Movie:
    for item in movies:
        if item["id"] == id:
            return JSONResponse(content=item)
    return JSONResponse(content=[])

@app.get('/movies/', tags=['movies'], response_model=List[Movie])
def get_movies_by_category(category: str = Query(min_length= 5, max_length= 15)) -> list[Movie]:
    data = [item for item in movies if item["category"] == category]
    return JSONResponse(content=data)

# Metodo create 
@app.post('/movies', tags=['movies'], response_model=dict)
def create_movies(movie: Movie) -> dict:
    movies.append(movie)
    return JSONResponse(content={"message": "Se ha registrado la pelicula"})

# Metodo update
@app.put('/movies/{id}', tags=['movies'], response_model=dict)
def update_movies(id: int, movie: Movie)-> dict:
    for item in  movies:
        if item["id"] == id:
            item["title"] = movie.title
            item["overview"] = movie.overview
            item["year"] = movie.year
            item["rating"] = movie.rating
            item["category"] = movie.category
            return JSONResponse(content={"message": "Se ha modificado la pelicula"})

# Metodo delete
@app.delete('/movies/{id}', tags=['movies'], response_model=dict)
def delete_movies(id: int)-> dict:
    for item in movies:
        if item["id"] == id:
            movies.remove(item)
            return JSONResponse(content={"message": "Se ha eliminado la pelicula"})
