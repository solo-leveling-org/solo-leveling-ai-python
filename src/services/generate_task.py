from src.config.ai_config import create_chat_client
from src.prompt.task_prompt import generate_task_user_prompt
from src.model.generate_task_response import Task


def generate_task(topics: list[str], rarity: str) -> Task:
    chain = create_chat_client()
    user_input = generate_task_user_prompt(topics, rarity)
    task = chain.invoke({"input": user_input})
    return task
