from core.buzzer import RpiBuzzer
from core.led import LedOutput
from concurrent.futures import ProcessPoolExecutor
from core.lcd import LCD
import asyncio

buzzer = RpiBuzzer()
led = LedOutput()
lcd = LCD()

if __name__ == "__main__":
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(LCD.print_something()), loop.create_task(buzzer.boo_beep())]
    
    loop.run_until_complete(asyncio.wait(tasks))
    
    loop.close()

