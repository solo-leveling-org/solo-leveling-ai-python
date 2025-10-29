import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda, Runnable
from langchain.output_parsers import PydanticOutputParser
from src.prompt.task_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
from src.models.generate_task_response import Task
from src.config.config_loader import config
from pydantic import SecretStr


load_dotenv()
api_key = os.getenv("OPENAI_ROUTER_KEY")
api_key_secret = SecretStr(api_key) if api_key else None


def create_chat_client() -> Runnable:
    parser = PydanticOutputParser(pydantic_object=Task)

    model_config = config["ai"]["gemini"]
    llm = ChatOpenAI(
        model=model_config["name"],
        base_url=model_config["api_base"],
        temperature=model_config["temperature"],
        max_completion_tokens=model_config.get("max_tokens", 1024),
        timeout=model_config.get("timeout", 30),
        api_key=api_key_secret,
    )

    prompt = ChatPromptTemplate.from_messages(
        [("system", SYSTEM_PROMPT), ("user", "{input}")]
    )

    chat_client = (
        prompt | llm | StrOutputParser() | RunnableLambda(lambda x: parser.parse(x))
    )

    return chat_client
