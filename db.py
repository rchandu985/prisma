from prisma import Prisma
from datetime import datetime
import asyncio
from prisma.errors import UniqueViolationError

class PrismaNextGen:

    async def Create():
        try:
            prisma  :   Prisma  =   Prisma()    
            await prisma.connect()

            await prisma.files.create(data={
            'file_id':"video_file",
            "file_name":"ram",
            "uploaded_at":datetime.now()
            })

            

            await prisma.disconnect()

        except UniqueViolationError:
            print("file allready exists")
    
    async def FindOne():
        
        prisma  :   Prisma  =   Prisma()    
        await prisma.connect()

        data =  await prisma.files.update(where={"file_name":"ram"},data={})
        print(data,type(data))
        await prisma.disconnect()

    async def FindMany():

        prisma  :   Prisma  =   Prisma()    
        await prisma.connect()

        data =  await prisma.files.find_many()
        print(data)
        await prisma.disconnect()


    async def Update():
        try:
            prisma  :   Prisma  =   Prisma()    
            await prisma.connect()

            await prisma.files.update(where={"file_name":"chandu"},data={"uploaded_at":datetime.now()})

            await prisma.disconnect()

        except UniqueViolationError:
            print("file allready exists")

    async def Delete():
        prisma  :   Prisma  =   Prisma()    
        await prisma.connect()
        
        deleted     =   await prisma.files.delete(where={"file_id":"frc"})

        print(deleted)
        
        await prisma.disconnect()
    
    async def DeleteMany():
        prisma  :   Prisma  =   Prisma()    
        await prisma.connect()
        
        deleted     =   await prisma.files.delete_many()

        print(deleted)
        
        await prisma.disconnect()




