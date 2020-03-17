from gpiozero import Buzzer
import asyncio


class RpiBuzzer:
    def __init__(self, buzzer_pin=13):
        self._bz = Buzzer(buzzer_pin)

    async def make_noise(self, delay: float):
        for i in range(100):
            self._bz.on()
            await asyncio.sleep(delay)
            self._bz.off()

    async def boo_beep(self, first_sound=0.001, second_sound=0.0000001, sleep=0.0000001):
        """
        I'm creative I know
        """
        await self.make_noise(first_sound)
        await asyncio.sleep(sleep)
        await self.make_noise(second_sound)
