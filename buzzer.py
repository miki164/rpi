from gpiozero import Buzzer
import asyncio


class RpiBuzzer:
    def __init__(self):
        self.bz = Buzzer(13)

    async def make_noise(self, delay: float):
        for i in range(100):
            self.bz.on()
            await asyncio.sleep(delay)
            self.bz.off()

    async def boo_beep(self, first_sound=0.0001, second_sound=0.0000001, sleep=0.000001):
        """
        I'm creative I know
        """
        await self.make_noise(first_sound)
        await asyncio.sleep(sleep)
        await self.make_noise(second_sound)
