import logging
import asyncio
from faststream.kafka import KafkaBroker
from dishka.integrations.faststream import inject, FromDishka
from src.services.task_service import TaskService
from src.models.task_request import TaskRequest

logger = logging.getLogger(__name__)


def register_consumers(broker: KafkaBroker):
    @broker.subscriber("task.requests")
    @inject
    async def handle_task_request(
        task_request: TaskRequest,
        task_service: FromDishka[TaskService],
    ):
        logger.info(f"Received task request from microservice X: {task_request}")

        try:
            logger.info(
                f"Generating task for topics: {task_request.topics}, rarity: {task_request.rarity}"
            )
            task = await asyncio.to_thread(
                task_service.generate_task,
                topics = task_request.topics,
                rarity = task_request.rarity,
            )

            logger.info(f"Generated task: {task}")

            await broker.publish(task.model_dump(), topic="task.responses")
            logger.info("📤 Sent task to microservice Y (topic: task.responses)")

        except Exception as e:
            logger.error(f"Error processing task request: {e}")

            error_response = {
                "error": str(e),
                "original_request": task_request.model_dump(),
                "status": "failed",
            }
            await broker.publish(error_response, topic="task.errors")
            logger.error("Sent error to topic: task.errors")

    logger.info("Consumer registered for topic 'task.requests'")
