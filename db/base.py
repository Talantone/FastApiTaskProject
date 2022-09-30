from core.config import DATABASE_URL
import motor.motor_asyncio
from beanie import init_beanie

from models.user import User
from models.tasks import Task


async def initiate_database():
    client = motor.motor_asyncio.AsyncIOMotorClient(DATABASE_URL)
    await init_beanie(database=client.get_default_database(),
                      document_models=[User, Task])
