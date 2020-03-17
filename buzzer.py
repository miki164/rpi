from gpiozero import Buzzer
import asyncio


class RpiBuzzer:
    def __init__(self):
        self.bz = Buzzer(13)

    async def make_beep(self, delay: float):
        for i in range(100):
            self.bz.on()
            await asyncio.sleep(delay)
            self.bz.off()
