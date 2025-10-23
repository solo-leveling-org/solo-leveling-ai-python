from src.prompt.task_prompt import generate_task_user_prompt
from src.model.generate_task_response import Task

class TaskService:
    def __init__(self, chat_client):
        self.chat_client = chat_client

    def generate_task(self, topics: list[str], rarity: str) -> Task:
        user_input = generate_task_user_prompt(topics, rarity)
        task = self.chat_client.invoke({"input": user_input})
        return task