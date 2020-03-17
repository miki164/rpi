from buzzer import RpiBuzzer
import asyncio

buzzer = RpiBuzzer()
loop = asyncio.get_event_loop()
resp = loop.run_until_complete(buzzer.test())
print(resp)