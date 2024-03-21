from time import sleep, strftime, time
from gpio import CPUTemperature
import matplotlib.pyplot as plt

cpu = CPUTemperarture()

plt.ion()
x = []
y = []
