import matplotlib.pyplot as plt
import numpy as np


with open("settings.txt", "r") as settings:
    tmp = [float(i) for i in settings.read().split("\n")]
    print(tmp)

data_array = np.loadtxt("data.txt", dtype=float)

period = tmp[0]

print (data_array.size)
print (period)

# создение массива для значений горизонтальной оси
x = np.linspace(0, period * data_array.size, data_array.size)
time_chrg = data_array.argmax() * period
time_rchrg = (data_array.size - data_array.argmax()) * period

# Decoration
fig, ax = plt.subplots(figsize=(16, 10), dpi=400)

# создаем график с названием ax. LABEL - название легенды
ax.plot (x, data_array, marker=".", color="blue", label="U(t)")

# добавление легенды
ax.legend(fontsize = 22)

# добавление разметки
ax.grid (axis='both', alpha=1, linestyle = "--")

# добавление заголовка и подписей ко всем осям
ax.set_title("Process of charging and recharging of condensateur", fontsize = 32)
ax.set_xlabel ("Time of measuring t, c", fontsize = 22)
ax.set_ylabel ("Voltage U, В", fontsize = 22)

# добавление текстовых вставок
ax.text(40, 2.5, "Time of charging: {:.3f} c".format(time_chrg), fontsize = 15)
ax.text(40, 2, "Time of recharging: {:.3f} c".format(time_rchrg), fontsize = 15)

# сохранение графика в файл
fig.savefig("test.png")