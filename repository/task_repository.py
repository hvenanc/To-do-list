from typing import List, Optional
from config.firebase_config import db
from schemas.to_do_list import ToDoListRequest, ToDoListResponse, helper


class TaskRepository:


    def __init__(self):
        self.collection = db.collection("to_do_list")


    def create(self, task: ToDoListRequest):
        doc_ref = self.collection.document(task.id)
        doc_ref.set(task.model_dump())
        return task


    def get_all(self):
        docs = self.collection.stream()
        return [helper(doc) for doc in docs]
    

    def get_by_id(self, id: str):
        doc = self.collection.document(id).get()
        return helper(doc) if doc.exists else None
    

    def update(self, id: str, task: ToDoListRequest):
        doc_ref = self.collection.document(id)
        doc_ref.update(task)
        return doc_ref.get()

    
    def delete(self, id: str) -> bool:
        doc_ref = self.collection.document(id)
        doc_ref.delete()
        return True
