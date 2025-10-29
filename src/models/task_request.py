from pydantic import BaseModel
from typing import List


class TaskRequest(BaseModel):
    topics: List[str]
    rarity: str
