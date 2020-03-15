from gpiozero import Buzzer

bz = Buzzer(13)
while True:
    bz.on()
    bz.off()