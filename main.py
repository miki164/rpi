from gpiozero import TonalBuzzer
from gpiozero.tones import Tone
from gpiozero.tools import sin_values
from time import sleep

tb = TonalBuzzer(20)
for note in 'C4 D4 E4 F4 G4 A4 B4 C5'.split():
    tone = Tone(note)
    print(repr(tone))
    tb.play(tone)
    sleep(0.3)

tb.stop()