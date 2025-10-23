import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain.output_parsers import PydanticOutputParser
from src.prompt.task_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
from src.model.generate_task_response import Task
from src.config.config_loader import config


load_dotenv()
api_key = os.getenv("OPENAI_ROUTER_KEY")


def create_chat_client():
    parser = PydanticOutputParser(pydantic_object=Task)

    model_config = config["ai"]["gemini"]
    llm = ChatOpenAI(
        model=model_config["name"],
        openai_api_base=model_config["api_base"],
        temperature=model_config["temperature"],
        max_tokens=model_config.get("max_tokens", 1024),
        timeout=model_config.get("timeout", 30),
        api_key=os.getenv("OPENAI_ROUTER_KEY"),
    )

    prompt = ChatPromptTemplate.from_messages(
        [("system", SYSTEM_PROMPT), ("user", "{input}")]
    )

    chat_client = prompt | llm | StrOutputParser() | RunnableLambda(lambda x: parser.parse(x))

    return chat_client
