import logging
from faststream import Context
from faststream.kafka import KafkaBroker
from dishka import Container
from src.services.task_service import TaskService

logger = logging.getLogger(__name__)


def register_consumers(broker: KafkaBroker):
    @broker.subscriber("task.requests")
    async def handle_task_request(
        task_request: dict,
        container: Container = Context(),
    ):
        logger.info(f"Received task request: {task_request}")
        task_service = container.get(TaskService)

        task = task_service.generate_task(
            topics=task_request["topics"], rarity=task_request["rarity"]
        )

        logger.info(f"Generated task: {task}")
    # await broker.publish(task.dict(), topic="task.responses")
