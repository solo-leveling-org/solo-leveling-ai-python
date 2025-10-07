from pydantic import BaseModel


class Task(BaseModel):
    title: str
    description: str
    experience: int
    currencyReward: int
    agility: int
    strength: int
    intelligence: int
