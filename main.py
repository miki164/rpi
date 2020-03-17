from buzzer import RpiBuzzer
import asyncio

buzzer = RpiBuzzer()
asyncio.run(buzzer.make_beep(0.002))
