from fastapi import FastAPI
from fastapi.responses import HTMLResponse
from config.database import engine, Base
from middlewares.error_handler import Error_Handler as ErrorHandler
from routers.movie import movie_router
from routers.user import user_router


app = FastAPI()

# cambiar el nombre de la aplicación
app.title = "Mi aplicación con FastAPI"

# cambiar la version de la aplicación
app.version = "0.0.1"

app.add_middleware(ErrorHandler)
app.include_router(movie_router)
app.include_router(user_router)

Base.metadata.create_all(bind=engine)


movies = [
    {
        "id": 1,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Acción",
    },
    {
        "id": 2,
        "title": "Avatar",
        "overview": "En un exuberante planeta llamado Pandora viven los Na'vi, seres que ...",
        "year": "2009",
        "rating": 7.8,
        "category": "Accion",
    },
]

# los tags nos permite agrupar las rutas de la aplicación


@app.get("/", tags=["home"])
def message():
    return HTMLResponse("<h1>Hello world!</h1>")
