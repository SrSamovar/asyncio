import asyncio
from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String, JSON
from sqlalchemy.orm import sessionmaker


Base = declarative_base()


class Person(Base):
    __tablename__ = 'swapi_people'

    id = Column(Integer, primary_key=True)
    name = Column(String)
    height = Column(String)
    mass = Column(String)
    hair_color = Column(String)
    skin_color = Column(String)
    eye_color = Column(String)
    birth_year = Column(String)
    gender = Column(String)
    homeworld = Column(String)
    films = Column(JSON)
    species = Column(JSON)
    vehicles = Column(JSON)
    starships = Column(JSON)
    created = Column(String)
    edited = Column(String)


DATABASE_URL = "postgresql+asyncpg://postgres:LSamovar69@localhost/swapi"
engine = create_async_engine(DATABASE_URL, echo=True)

AsyncSessionLocal = sessionmaker(engine, class_=AsyncSession, expire_on_commit=False)


async def create_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.create_all)


async def drop_table():
    async with engine.begin() as conn:
        await conn.run_sync(Base.metadata.drop_all)


async def add_person(person_id, person_data):
    async with AsyncSessionLocal() as session:
        if person_data is None:
            return
        new_person = Person(
            id=person_id,
            name=person_data.get('name'),
            height=person_data.get('height'),
            mass=person_data.get('mass'),
            hair_color=person_data.get('hair_color'),
            skin_color=person_data.get('skin_color'),
            eye_color=person_data.get('eye_color'),
            birth_year=person_data.get('birth_year'),
            gender=person_data.get('gender'),
            homeworld=person_data.get('homeworld'),
            films=person_data.get('films'),
            species=person_data.get('species'),
            vehicles=person_data.get('vehicles'),
            starships=person_data.get('starships'),
            created=person_data.get('created'),
            edited=person_data.get('edited')
        )
        session.add(new_person)
        await session.commit()


