from buzzer import RpiBuzzer
from led import LedOutput
from concurrent.futures import ProcessPoolExecutor
from lcd import LCD
import asyncio

buzzer = RpiBuzzer()
led = LedOutput()
lcd = LCD()

if __name__ == "__main__":
    executor = ProcessPoolExecutor(2)
    loop = asyncio.get_event_loop()
    tasks = [loop.create_task(lcd.print_something()), loop.create_task(buzzer.boo_beep())]
    
    loop.run_until_complete(asyncio.wait(tasks))
    
    loop.close()

