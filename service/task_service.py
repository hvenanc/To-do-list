from typing import List, Optional
from schemas.task import TaskRequest, TaskResponse, helper
from repository.task_repository import TaskRepository


class TaskService:


    def __init__(self):
        self.repository = TaskRepository()

    
    def create(self, task: TaskRequest) -> TaskResponse:
        doc = self.repository.collection.document()
        create_task = TaskResponse(
            id = doc.id,
            nome = task.nome,
            descricao = task.descricao,
            prioridade = task.prioridade,
            status = task.status if task.status else False
        )
        return self.repository.create(create_task)
    

    def get_all(self) -> List[TaskResponse]:
        return self.repository.get_all()
    

    def get_by_id(self, id: str) -> Optional[TaskResponse]:
        return self.repository.get_by_id(id)
    

    def update(self, id: str, task: TaskRequest) -> Optional[TaskResponse]:

        task_update = self.repository.get_by_id(id)

        if not task_update:
            return None
        
        else:
            task = self.repository.update(id, task.model_dump(exclude_unset=True))
            return helper(task)
        

    def delete(self, id):

        task = self.repository.get_by_id(id)

        if not task:
            return None
        return self.repository.delete(id)