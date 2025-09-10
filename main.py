from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from routes.task_routes import TaskController


app = FastAPI(
    title="API de Gerenciamento de Tarefas",
    version= "1.0",
    description="TO-DO-LIST"
)

controller = TaskController()
app.include_router(controller.router)


# Configuração do CORS para ser público
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permite todas as origens
    allow_credentials=True,
    allow_methods=["*"],  # Permite todos os métodos HTTP (GET, POST, PUT, DELETE, etc.)
    allow_headers=["*"],  # Permite todos os cabeçalhos
)