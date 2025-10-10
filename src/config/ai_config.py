import os
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from langchain.output_parsers import PydanticOutputParser
from src.prompt.task_prompt import SYSTEM_PROMPT
from dotenv import load_dotenv
from src.model.generate_task_response import Task


load_dotenv()
api_key=os.getenv("OPENAI_ROUTER_KEY")


def create_chat_client():
    parser = PydanticOutputParser(pydantic_object=Task)

    llm = ChatOpenAI(
        model="google/gemini-2.0-flash-lite-001",
        openai_api_base="https://openrouter.ai/api/v1",
        temperature=1,
        api_key=api_key

    )

    prompt = ChatPromptTemplate.from_messages([
        ("system", SYSTEM_PROMPT),
        ("user", "{input}")
    ])

    chain = prompt | llm | StrOutputParser() | RunnableLambda(lambda x: parser.parse(x))

    return chain

