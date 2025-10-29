import asyncio
import logging
from faststream import FastStream
from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka
from src.di.providers import (
    ConfigProvider,
    LLMProvider,
    TaskServiceProvider,
    FastStreamProvider,
)
from src.kafka.consumer import broker

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info("Starting Kafka consumer service...")
    container = make_async_container(
        ConfigProvider(), LLMProvider(), TaskServiceProvider(), FastStreamProvider()
    )

    setup_dishka(container=container, broker=broker, auto_inject=True)

    app = FastStream(broker)

    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
