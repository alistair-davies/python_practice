import matplotlib
matplotlib.use("TkAgg")

import pandas as pd
import matplotlib.pyplot as plt 

df = pd.read_csv("test_blackbox.csv", skiprows=150)
#print(df.head())
#print(df.columns)

gps = df[(df["GPS_coord[0]"] != 0) & (df["GPS_coord[1]"] != 0)]

plt.plot(df["time"], df["motor[0]"], label="Motor 0")
plt.plot(df["time"], df["motor[1]"], label="Motor 1")
plt.plot(df["time"], df["motor[2]"], label="Motor 2")
plt.plot(df["time"], df["motor[3]"], label="Motor 3")

plt.xlabel("Time")
plt.ylabel("Motor Output")
plt.title("Motor Outputs Over Time")
plt.legend()
plt.show()

plt.close()

















"""
plt.plot(df["time"], df["gyroADC[0]"], label="Roll")
plt.plot(df["time"], df["gyroADC[1]"], label="Pitch")
plt.plot(df["time"], df["gyroADC[2]"], label="Yaw")
plt.legend()
plt.show()
"""


"""
plt.figure(figsize=(8, 8))
plt.scatter(
    gps["GPS_coord[1]"],
    gps["GPS_coord[0]"],
    c=gps["GPS_speed"],
    cmap="viridis",
    s=8
)

plt.colorbar(label="Speed (m/s)")
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title("GPS Flight Path (Coloured by Speed)")
plt.grid(True)
plt.show(block=False)
"""
