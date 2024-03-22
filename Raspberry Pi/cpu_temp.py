from time import sleep, strftime, time
from gpio import CPUTemperature
import matplotlib.pyplot as plt

cpu = CPUTemperarture()

plt.ion()
x = []
y = []

def write_temp(temp):
  with open(".home/username/cpu_temp.csv", "a") as log:
    log.write("{0},{1}\n".format(strftime("%Y-%m-%d %H:%M:%S"), str(temp)))

