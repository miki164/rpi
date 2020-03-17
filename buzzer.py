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

    async def boo_beep(self):
        """
        I'm creative I know
        """
        await self.make_noise(0.0003)
        await asyncio.sleep(0.0000001)
        await self.make_noise(0.0000001)
