from fastapi import FastAPI
from routes.user import user 

app = FastAPI(
    title="Lo que tanto me pidio",
    description="aca esta la primera API para mi amigo Baud",
    openapi_tags=[{"name":"Usuarios", "description": "Opciones Usuarios"}]
)

app.include_router(user)