from pydantic import BaseModel


class ToDoListRequest(BaseModel):
    nome: str
    descricao: str
    prioridade: int
    status: bool = True


class ToDoListResponse(BaseModel):
    id: str
    nome: str
    descricao: str
    prioridade: int
    status: bool


def helper(doc) -> dict:
    data = doc.to_dict()
    data["id"] = doc.id
    return data