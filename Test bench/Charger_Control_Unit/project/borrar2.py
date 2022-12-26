
import asyncio
import time

class reposit:
    valor = 10
    def __init__(self):
        print("iniciamos clase")

    async def prueba1(self):
        while True:
            self.valor += 1
            await asyncio.sleep(0.2)

    async def prueba2(self):
        while True:
            print(self.valor)
            await asyncio.sleep(1)

cc = reposit()
print(cc.valor)

loop = asyncio.get_event_loop()             # Sirve para iniciar una cola de loop que se va a ejecutar
try:
    #asyncio.ensure_future(firstWorker())    # Este comando se usa para introducirlos en la cola del loop, para asi correrlo despues
    #asyncio.ensure_future(secondWorker())
    asyncio.ensure_future(cc.prueba1())
    asyncio.ensure_future(cc.prueba2())

    loop.run_forever()                      # Con run forever, cuando terminan todas las funciones, se vuelve a empezar el proceso
except KeyboardInterrupt:
    pass
finally:
    print("Closing Loop")
    loop.close()
