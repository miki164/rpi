from buzzer import RpiBuzzer
import asyncio

buzzer = RpiBuzzer()
loop = asyncio.get_event_loop()
loop.run_until_complete(buzzer.boo_beep())
