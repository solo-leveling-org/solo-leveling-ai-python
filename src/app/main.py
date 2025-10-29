import asyncio
import logging
from faststream import FastStream
from faststream.kafka import KafkaBroker
from dishka import make_async_container
from dishka.integrations.faststream import setup_dishka
from src.kafka.consumer import register_consumers
from src.di.providers import (
    ConfigProvider,
    LLMProvider,
    TaskServiceProvider,
    FastStreamProvider,
)

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)


async def main():
    logger.info("Starting Kafka consumer service...")
    container = make_async_container(
        ConfigProvider(), LLMProvider(), TaskServiceProvider(), FastStreamProvider()
    )
    broker = await container.get(KafkaBroker)
    setup_dishka(container=container, broker=broker, auto_inject=True)
    register_consumers(broker)
    app = FastStream(broker)

    await app.run()


if __name__ == "__main__":
    asyncio.run(main())
