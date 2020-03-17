from buzzer import RpiBuzzer
from led import LedOutput
import asyncio

buzzer = RpiBuzzer()
led = LedOutput()
asyncio.run(buzzer.boo_beep())
asyncio.run(led.blink())
