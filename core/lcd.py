from RPLCD.i2c import CharLCD


class LCD:
    def __init__(self):
        self.lcd = CharLCD('PCF8574', 0x27)

    async def print_something(self, text: str, row=0, col=0) -> None:
        self.lcd.clear()
        self.lcd.cursor_pos(row, col)
        self.lcd.write_string(text)
