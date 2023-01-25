from fastapi import FastAPI

app = FastAPI()

# cambiar el nombre de la aplicación
app.title = "Mi aplicación con FastAPI"

# cambiar la version de la aplicación
app.version = "0.0.1"

# los tags nos permite agrupar las rutas de la aplicación

@app.get('/', tags=['home'])
def message():
    return "Hello world!!!"