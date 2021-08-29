from sqlalchemy.ext.asyncio import AsyncSession, create_async_engine
from sqlalchemy.orm import sessionmaker


async def get_session() -> AsyncSession:
    async with async_session() as session:
        yield session
