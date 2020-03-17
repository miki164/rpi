from buzzer import RpiBuzzer
from led import LedOutput
from concurrent.futures import ProcessPoolExecutor
import asyncio

buzzer = RpiBuzzer()
led = LedOutput()

if __name__=="__main__": 
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(led.blink(20)),loop.create_task(buzzer.boo_beep())]
    
    loop.run_until_complete(asyncio.wait(tasks))
    
    loop.close()

