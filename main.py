from buzzer import RpiBuzzer
import asyncio

buzzer = RpiBuzzer()
asyncio.run(buzzer.boo_beep())
