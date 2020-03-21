from gpiozero import LED
import asyncio


class LedOutput:
    def __init__(self, led_pin=20):
        self._led = LED(led_pin)

    async def blink(self, delay=1):
        self._led.on()
        await asyncio.sleep(delay)
        self._led.off()

    async def turn_on(self):
        self._led.on()

    async def turn_off(self):
        self._led.off()
