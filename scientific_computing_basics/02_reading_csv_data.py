"""Read, clean, and plot a small scientific dataset.

Run this file cell by cell in VS Code after activating the
``scientific-basics`` Conda environment.
"""

# %% 1. Import pandas and matplotlib
import matplotlib.pyplot as plt
import pandas as pd

print("Tools are ready!")

# %% 2. Read the CSV file
data = pd.read_csv("02_reading_csv_data.csv")

print(data)

# %% 3. Inspect the data
print("Column names:", list(data.columns))
print("Number of rows and columns:", data.shape)
print("Missing values in each column:")
print(data.isna().sum())

# %% 4. Clean the missing temperature
data["temperature_c"] = data["temperature_c"].interpolate()

print("Cleaned data:")
print(data)

# %% 5. Calculate useful summaries
average_temperature = data["temperature_c"].mean()
total_rainfall = data["rainfall_mm"].sum()
warmest_row = data.loc[data["temperature_c"].idxmax()]

print(f"Average temperature: {average_temperature:.1f} °C")
print(f"Total rainfall: {total_rainfall:.1f} mm")
print(
    f"Warmest day: {int(warmest_row['day'])} "
    f"({warmest_row['temperature_c']:.1f} °C)"
)

# %% 6. Filter rows with a simple question
warm_days = data[data["temperature_c"] > 20]

print("Days warmer than 20 °C:")
print(warm_days[["day", "temperature_c"]])

# %% 7. Plot the cleaned temperatures
fig, ax = plt.subplots(figsize=(7, 4))
ax.plot(
    data["day"],
    data["temperature_c"],
    marker="o",
    color="steelblue",
)
ax.set_title("Daily temperature")
ax.set_xlabel("Day")
ax.set_ylabel("Temperature (°C)")
ax.set_xticks(data["day"])
fig.tight_layout()
plt.show()

# %% 8. Save the cleaned data
data.to_csv("02_reading_csv_data_cleaned.csv", index=False)
print("Saved 02_reading_csv_data_cleaned.csv")
