from gpiozero import Buzzer

bz = Buzzer(3)
while True:
    bz.on()
    bz.off()