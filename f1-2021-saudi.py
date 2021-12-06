import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt
from matplotlib.pyplot import figure
import numpy as np
import pandas as pd

# Setup plotting
plotting.setup_mpl()

# Enable the cache
ff1.Cache.enable_cache('./f1-cache') 

# Get rid of some pandas warnings that are not relevant for us at the moment
pd.options.mode.chained_assignment = None 

# Load the session data
race = ff1.get_session(2021, 'Saudi', 'R')

# Get the laps
laps = race.load_laps(with_telemetry=True)

# Get laps of the drivers (HAM and VER)
laps_ham = laps.pick_driver('HAM')
laps_ver = laps.pick_driver('VER')

# Subtract formation lap
laps_ham['RaceLapNumber'] = laps_ham['LapNumber'] - 1
laps_ver['RaceLapNumber'] = laps_ver['LapNumber'] - 1

full_distance_ver_ham = pd.DataFrame()
summarized_distance_ver_ham = pd.DataFrame()

plt.rcParams['figure.figsize'] = [15, 6]

fig, ax = plt.subplots()
fig.suptitle("Saudi: HAM vs VER laps 18-50")

ax.plot(laps_ham['RaceLapNumber'], laps_ham['LapTime'], label='HAM', color='cyan', linewidth=5)
ax.plot(laps_ver['RaceLapNumber'], laps_ver['LapTime'], label='VER', color='pink', linewidth = 3)
ax.set(ylabel='Lap Time', xlabel='Lap Number')
ax.legend(loc="upper center")

plt.xlim([18, 50])
plt.show()

# Get lap data
lap_telemetry_ham = laps_ham.loc[laps_ham['RaceLapNumber']==36].get_car_data().add_distance()
lap_telemetry_ver = laps_ver.loc[laps_ver['RaceLapNumber']==36].get_car_data().add_distance()

# Make plot a bit bigger
plt.rcParams['figure.figsize'] = [15, 15]

fig, ax = plt.subplots(5)
fig.suptitle("Lap 37 Telemetry")

ax[0].title.set_text("Speed")
ax[0].plot(lap_telemetry_ham['Distance'], lap_telemetry_ham['Speed'], label='HAM', color='cyan', linewidth=2)
ax[0].plot(lap_telemetry_ver['Distance'], lap_telemetry_ver['Speed'], label='VER', color='pink', linewidth=2)
ax[0].set(ylabel='Speed')
ax[0].legend(loc="lower right")

ax[1].title.set_text("Throttle")
ax[1].plot(lap_telemetry_ham['Distance'], lap_telemetry_ham['Throttle'], label='HAM', color='cyan', linewidth=2)
ax[1].plot(lap_telemetry_ver['Distance'], lap_telemetry_ver['Throttle'], label='VER', color='pink', linewidth=2)
ax[1].set(ylabel='Throttle')

ax[2].title.set_text("Brake")
ax[2].plot(lap_telemetry_ham['Distance'], lap_telemetry_ham['Brake'], label='HAM', color='cyan', linewidth=2)
ax[2].plot(lap_telemetry_ver['Distance'], lap_telemetry_ver['Brake'], label='VER', color='pink', linewidth=2)
ax[2].set(ylabel='Brakes')

ax[3].title.set_text("Gears")
ax[3].plot(lap_telemetry_ham['Distance'], lap_telemetry_ham['nGear'], label='HAM', color='cyan', linewidth=2)
ax[3].plot(lap_telemetry_ver['Distance'], lap_telemetry_ver['nGear'], label='VER', color='pink', linewidth=2)
ax[3].set(ylabel='Gear')

ax[4].title.set_text("DRS")
ax[4].plot(lap_telemetry_ham['Distance'], lap_telemetry_ham['DRS'], label='HAM', color='cyan', linewidth=2)
ax[4].plot(lap_telemetry_ver['Distance'], lap_telemetry_ver['DRS'], label='VER', color='pink', linewidth=2)
ax[4].set(ylabel='DRS')

# Hide x labels and tick labels for top plots and y ticks for right plots.
for a in ax.flat:
    a.label_outer()

plt.show()