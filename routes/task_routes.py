from fastapi import APIRouter, HTTPException
from typing import List, Optional
from schemas.task import TaskRequest, TaskResponse
from service.task_service import TaskService


class TaskController:


    def __init__(self):
        self.router = APIRouter(
            prefix="tasks",
            tags=["TO-DO-LIST"]
        )
        self.service = TaskService()
        self._add_routes()


    def _add_routes(self):
        self.router.post("/", response_model=TaskResponse, status_code=201)(self.create)
        self.router.get("/", response_model=List[TaskResponse], status_code=200)(self.get_all)
        self.router.get("/{id}", response_model=Optional[TaskResponse], status_code=200)(self.get_by_id)
        self.router.put("/{id}", response_model=Optional[TaskResponse], status_code=200)(self.update)
        self.router.delete("/{id}", status_code=204)(self.delete)
        

    async def create(self, task: TaskRequest):
        return self.service.create(task)
    

    async def get_all(self):
        return self.service.get_all()
    

    async def get_by_id(self, id: str):
        task = self.service.get_by_id(id)

        if task:
            return task
        raise HTTPException(404, detail="Tarefa não localizada!")
    

    async def update(self, id: str, data: TaskRequest):

        task = self.service.get_by_id(id)

        if task:
            return self.service.update(id, data)
        raise HTTPException(404, detail="Tarefa não localizada!")
    

    async def delete(self, id: str):
        task = self.service.get_by_id(id)

        if task:
            self.service.delete(id)
        else:
            raise HTTPException(404, detail="Tarefa não localizada!")