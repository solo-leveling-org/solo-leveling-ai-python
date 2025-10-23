import logging
from dishka import make_container
from src.di.providers import ConfigProvider, LLMProvider, TaskServiceProvider
from src.services.task_service import TaskService

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Starting model test...")

    container = make_container(ConfigProvider(), LLMProvider(), TaskServiceProvider())

    try:
        # Dishka создаёт REQUEST-scoped объект **внутри контекста**
        with container() as request_container:
            task_service = request_container.get(TaskService)
            task = task_service.generate_task(["PHYSICAL_ACTIVITY", "MENTAL_HEALTH"], "EPIC")
            logger.info(f"Generated task: {task}")
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)


if __name__ == "__main__":
    main()