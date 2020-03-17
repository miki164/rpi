from gpiozero import Buzzer


class RpiBuzzer:
    def __init__(self):
        self.bz = Buzzer(13)

    async def make_beep(self):
        for i in range(100):
            await self.bz.on()
            await self.bz.off()