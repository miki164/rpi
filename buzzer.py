from gpiozero import Buzzer


class RpiBuzzer:
    def __init__(self):
        self.bz = Buzzer(13)

    async def make_beep(self):
        for i in range(100):
            self.bz.on()
            self.bz.off()