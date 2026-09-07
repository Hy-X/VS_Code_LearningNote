"""First steps in scientific computing.

Run this file cell by cell in VS Code, or run the complete file from a
terminal. The example uses made-up temperature measurements, so it works
without an internet connection or a downloaded data file.
"""

# %% 1. Import the tools
import matplotlib.pyplot as plt
import numpy as np

print("Scientific computing is ready!")

# %% 2. Create a small dataset
days = np.array([1, 2, 3, 4, 5])
temperatures = np.array([18.5, 19.0, 21.5, 23.0, 22.0])

print("Days:", days)
print("Temperatures (°C):", temperatures)

# %% 3. Calculate a summary
average = temperatures.mean()
lowest = temperatures.min()
highest = temperatures.max()
spread = temperatures.std()

print(f"Average: {average:.1f} °C")
print(f"Lowest: {lowest:.1f} °C")
print(f"Highest: {highest:.1f} °C")
print(f"Standard deviation: {spread:.1f} °C")

# %% 4. Write a small reusable function
def describe_measurements(values):
    """Print a short summary for a one-dimensional array of measurements."""
    print(f"Number of measurements: {values.size}")
    print(f"Average: {values.mean():.1f}")
    print(f"Range: {values.min():.1f} to {values.max():.1f}")


describe_measurements(temperatures)

# %% 5. Ask a simple question about the data
threshold = 20.0
warm_days = days[temperatures > threshold]

print(f"Days above {threshold:.1f} °C:", warm_days)

# %% 6. Plot the measurements
plt.style.use("seaborn-v0_8-whitegrid")

fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(days, temperatures, marker="o", color="steelblue", linewidth=2)
ax.axhline(average, color="darkorange", linestyle="--", label="Average")
ax.set_title("Temperature measurements")
ax.set_xlabel("Day")
ax.set_ylabel("Temperature (°C)")
ax.set_xticks(days)
ax.legend()
fig.tight_layout()
plt.show()

# %% 7. Practice: change these values and run the cell again
# Try your own five measurements. Then change the title or threshold above.
practice_temperatures = np.array([17.0, 18.5, 20.0, 21.0, 19.5])
describe_measurements(practice_temperatures)
