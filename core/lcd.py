from RPLCD.i2c import CharLCD


class LCD:
    def __init__(self):
        self.lcd = CharLCD('PCF8574', 0x27)

    def print_something(self):
        self.lcd.write_string('NIE NAWIDZĘ LUDZI KURWA MAĆ')

