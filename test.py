import asyncio

from db import PrismaNextGen

asyncio.run(PrismaNextGen.DeleteMany())