import logging
from src.services.generate_task import generate_task

logging.basicConfig(
    level=logging.INFO, format="%(asctime)s - %(name)s - %(levelname)s - %(message)s"
)

logger = logging.getLogger(__name__)


def main():
    logger.info("Starting model test...")

    try:
        task = generate_task(["PHYSICAL_ACTIVITY", "MENTAL_HEALTH"], "EPIC")
        logger.info(f"Generated task: {task}")
    except Exception as e:
        logger.error(f"Error: {e}", exc_info=True)


if __name__ == "__main__":
    main()
