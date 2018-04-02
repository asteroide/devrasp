# coding: utf-8
from gpiozero import CPUTemperature

cpu = CPUTemperature()
print("La température est : {}".format(cpu.temperature))
