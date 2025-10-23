import pytest
from dishka import make_container
from src.di.providers import ConfigProvider, LLMProvider, TaskServiceProvider
from src.services.task_service import TaskService

@pytest.mark.llm_integration
@pytest.mark.parametrize("rarity, min_exp, max_exp, max_attr", [
    ("COMMON", 10, 20, 2),
    ("UNCOMMON", 30, 40, 4),
    ("RARE", 50, 60, 6),
    ("EPIC", 70, 80, 8),
    ("LEGENDARY", 90, 100, 10)
])
def test_generate_task_with_all_rarities(rarity, min_exp, max_exp, max_attr):
    container = make_container(ConfigProvider(), LLMProvider(), TaskServiceProvider())

    with container() as request_container:
        task_service = request_container.get(TaskService)
        task = task_service.generate_task(["MENTAL_HEALTH"], rarity)

    assert min_exp <= task.experience <= max_exp
    assert task.currencyReward == task.experience // 2

    total_attrs = task.agility + task.strength + task.intelligence
    assert total_attrs <= max_attr

    assert task.title.strip()
    assert task.description.strip()

    assert 0 <= task.agility <= 10
    assert 0 <= task.strength <= 10
    assert 0 <= task.intelligence <= 10