import asyncio
import logging
from faststream import FastStream
from faststream.kafka import KafkaBroker
from dishka import make_async_container
from src.kafka.consumer import register_consumers
from dishka.integrations.faststream import setup_dishka
from src.di.providers import (
    ConfigProvider,
    LLMProvider,
    TaskServiceProvider,
    FastStreamProvider,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info("🚀 Starting Task Generator Microservice...")

    container = make_async_container(
        ConfigProvider(),
        LLMProvider(),
        TaskServiceProvider(),
        FastStreamProvider(),
    )

    broker = await container.get(KafkaBroker)
    logger.info("Kafka broker obtained from DI")

    setup_dishka(container=container, broker=broker, auto_inject=True)
    logger.info("Dishka integration configured")

    register_consumers(broker)
    logger.info("Consumers registered")

    app = FastStream(broker)
    logger.info("icroservice ready! Listening for task requests...")

    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
