from gpiozero import LED, Button
from time import sleep

LEDS = {"a": LED(2), 
        "g": LED(3), 
        "f": LED(4), 
        "e": LED(17), 
        "d": LED(27), 
        "b": LED(22), 
        "c": LED(23), 
        "point": LED(24)}

def aff(numero):
    if numero == 0:
        LEDS["a"].on()
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["f"].on()
    elif numero == 1:
        LEDS["c"].on()
        LEDS["d"].on()
    elif numero == 2:
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["g"].on()
        LEDS["e"].on()
        LEDS["f"].on()
    elif numero == 3:
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["g"].on()
        LEDS["d"].on()
        LEDS["e"].on()
    elif numero == 4:
        LEDS["a"].on()
        LEDS["g"].on()
        LEDS["c"].on()
        LEDS["d"].on()
    elif numero == 5:
        LEDS["b"].on()
        LEDS["a"].on()
        LEDS["g"].on()
        LEDS["d"].on()
        LEDS["e"].on()
    elif numero == 6:
        LEDS["b"].on()
        LEDS["a"].on()
        LEDS["g"].on()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["f"].on()
    elif numero == 7:
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].on()
    elif numero == 8:
        LEDS["a"].on()
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["f"].on()
        LEDS["g"].on()
    elif numero == 9:
        LEDS["a"].on()
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["g"].on()


#print("Allumage des leds...")
#for cle in ("a", "b", "c", "d", "e", "f", "g"):
#    LEDS[cle].on()
#    sleep(0.5)
#    LEDS[cle].off()
#    sleep(0.5)

#print("Extinction des leds...")
#sleep(1)
def noir():
    for cle in ("a", "b", "c", "d", "e", "f", "g"):
        LEDS[cle].off()

while True:
    for i in range(10):
        noir()
        aff(i)
        sleep(1)
noir()
sleep(4)

