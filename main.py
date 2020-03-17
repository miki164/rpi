from buzzer import RpiBuzzer
from led import LedOutput
from concurrent.futures import ProcessPoolExecutor
import asyncio

buzzer = RpiBuzzer()
led = LedOutput()

executor = ProcessPoolExecutor(2)
loop = asyncio.get_event_loop()
bz = asyncio.create_task(loop.run_in_executor(executor, buzzer.boo_beep))
l = asyncio.create_task(loop.run_in_executor(executor, led.blink))
