import fastf1 as ff1
from fastf1 import plotting
from matplotlib import pyplot as plt

plotting.setup_mpl()

ff1.Cache.enable_cache('./.f1-cache')  # optional but recommended

race = ff1.get_session(2020, 'Turkey', 'R')
laps = race.load_laps()

ver = laps.pick_driver('VER')
ham = laps.pick_driver('HAM')
fig, ax = plt.subplots()
ax.plot(ver['LapNumber'], ver['LapTime'], color='pink')
ax.plot(ham['LapNumber'], ham['LapTime'], color='cyan')
ax.set_title("Turkey: VER vs HAM")
ax.set_xlabel("Lap Number")
ax.set_ylabel("Lap Time")
plt.show()
