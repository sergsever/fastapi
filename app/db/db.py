# from sqlalchemy.orm import DeclarativeBase
# from sqlalchemy.ext.asyncio import create_async_engine, async_sessionmaker, AsyncAttrs
# from sqlalchemy.orm import DeclarativeBase, declared_attr
# from sqlalchemy import create_engine
from sqlmodel import Field, Session, SQLModel, create_engine
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession,async_sessionmaker
# class Base(DeclarativeBase):
#     pass

DB_HOST = 'localhost'
DB_PORT = '5432'
DB_NAME = 'postgres'
DB_USER = 'postgres'
DB_PASSWORD = 'ssl-2000'

DATABASE_URL = f'postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'
DATABASE_URL_ASYNC = f'postgresql+asyncpg://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}'

async_engine = create_async_engine(DATABASE_URL_ASYNC)

engine = create_engine(DATABASE_URL)        #create_async_engine(DATABASE_URL)
async_session_maker = async_sessionmaker(async_engine, expire_on_commit=False)

def connection(method):
    async def wrapper(*args, **kwargs):
        async with async_session_maker() as session:
            try:
                # Явно не открываем транзакции, так как они уже есть в контексте
                return await method(*args, session=session, **kwargs)
            except Exception as e:
                await session.rollback()  # Откатываем сессию при ошибке
                raise e  # Поднимаем исключение дальше
            finally:
                await session.close()  # Закрываем сессию

    return wrapper

def create_all():
    SQLModel.metadata.create_all(engine)

