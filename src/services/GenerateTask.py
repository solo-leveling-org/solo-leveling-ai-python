from src.config.AiConfig import create_chat_client
from src.prompt.TaskPrompt import generate_task_user_prompt
from src.model.GenerateTaskResponse import Task


def generate_task(topics: list[str], rarity: str) -> Task:
    chain = create_chat_client()
    user_input = generate_task_user_prompt(topics, rarity)
    task = chain.invoke({"input": user_input})
    return task
