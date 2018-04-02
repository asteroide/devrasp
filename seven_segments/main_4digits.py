from gpiozero import LED, Button
from time import sleep, strftime
import sys

LEDS = {
        "d1": LED(4), 
        "d2": LED(27),
        "d3": LED(17),
        "d4": LED(22), 
        "b": LED(18), 
        "c": LED(23), 
        "d": LED(24), 
        "e": LED(25), 
        "f": LED(5), 
        "a": LED(6), 
        "p": LED(13), 
        "g": LED(12), 
}


def set_digit(number="0000"):
    # for cpt in range(4):
    #     # print("set_digit={}".format(cpt))
    #     LEDS["d{}".format(cpt+1)].off()
    for cpt in range(4):
        # print("for={}".format(number[cpt]))
        if number[cpt] == "1":
            # print("Setting 1 to {}".format(cpt))
            LEDS["d{}".format(cpt+1)].on()
        # else:
        #     LEDS["d{}".format(cpt+1)].off()


def print_number(numero):
    if numero == 0:
        LEDS["a"].on()
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["f"].on()
        LEDS["g"].off()
    elif numero == 1:
        LEDS["a"].off()
        LEDS["b"].off()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].off()
        LEDS["f"].off()
        LEDS["g"].off()
    elif numero == 2:
        LEDS["a"].off()
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].off()
        LEDS["e"].on()
        LEDS["f"].on()
        LEDS["g"].off()
    elif numero == 3:
        LEDS["a"].off()
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["f"].off()
        LEDS["g"].on()
    elif numero == 4:
        LEDS["a"].on()
        LEDS["b"].off()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].off()
        LEDS["f"].off()
        LEDS["g"].on()
    elif numero == 5:
        LEDS["a"].on()
        LEDS["b"].on()
        LEDS["c"].off()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["f"].off()
        LEDS["g"].on()
    elif numero == 6:
        LEDS["a"].on()
        LEDS["b"].on()
        LEDS["c"].off()
        LEDS["d"].on()
        LEDS["e"].on()
        LEDS["f"].on()
        LEDS["g"].on()
    elif numero == 7:
        LEDS["a"].off()
        LEDS["b"].on()
        LEDS["c"].on()
        LEDS["d"].on()
        LEDS["e"].off()
        LEDS["f"].off()
        LEDS["g"].off()
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
        LEDS["f"].off()
        LEDS["g"].on()
    else:
        LEDS["a"].off()
        LEDS["b"].off()
        LEDS["c"].off()
        LEDS["d"].off()
        LEDS["e"].off()
        LEDS["f"].off()
        LEDS["g"].off()


def black_led():
    for cle in ("a", "b", "c", "d", "e", "f", "g", "p"):
        LEDS[cle].off()


def switch_digit(blank=True, number=0):
    if not number:
        for cle in ("d1", "d2", "d3", "d4"):
            if blank:
                LEDS[cle].on()
            else:
                LEDS[cle].off()
    else:
        if blank:
            LEDS["d{}".format(number)].on()
        else:
            LEDS["d{}".format(number)].off()


DIGIT_SEQ = (
    "1111",
    "0111",
    "1011",
    "1101",
    "1110",
    "1101",
    "1011",
    "0111",
)


def circle_digits():
    cpt = 0
    for seq in DIGIT_SEQ:
        print("Affichage {}".format(seq))
        black_led()
        set_digit(seq)
        print_number(cpt % 10)
        sleep(1)
        cpt += 1


def print_digit(digit, number):
    switch_digit(True)
    print_number(number % 10)
    sleep(0.0001)
    # print_number(-1)
    switch_digit(False, digit)
    sleep(0.002)


def snake():
    LEDS['d1'].off()
    LEDS['d2'].off()
    LEDS['d3'].off()
    LEDS['d4'].off()

    LEDS['d'].off()
    LEDS['a'].on()
    sleep(0.5)
    LEDS['e'].off()
    LEDS['b'].on()
    sleep(0.5)
    LEDS['f'].off()
    LEDS['c'].on()
    sleep(0.5)
    LEDS['a'].off()
    LEDS['d'].on()
    sleep(0.5)
    LEDS['b'].off()
    LEDS['e'].on()
    sleep(0.5)
    LEDS['c'].off()
    LEDS['f'].on()
    sleep(0.5)


def print_time(t=strftime("%H:%M")):

    print(t)
    for i in range(1000):
        t = strftime("%H:%M")
        print_digit(1, int(t[0]))
        print_digit(2, int(t[1]))
        print_digit(3, int(t[3]))
        print_digit(4, int(t[4]))
    # switch_digit(False)


if __name__ == "__main__":
    # for i in range(5): snake()
    print_time()
    # for cpt in range(4):
    #     sys.stdout.write("Stopping in {}             \n".format(4-cpt))
    #     sys.stdout.flush()
    #     sleep(1)
