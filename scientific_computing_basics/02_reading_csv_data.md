# Module 2: Reading and Cleaning CSV Data

In the first module, we typed measurements directly into a Python script. Real
scientific work usually starts with a data file. In this module, you will read
a CSV file, find a missing value, fill it, calculate summaries, and plot the
result.

CSV means **comma-separated values**. It is a simple text format that works
with spreadsheets and many scientific instruments.

## What you will learn

- read a CSV file with pandas,
- inspect rows, columns, and missing values,
- fill one missing measurement,
- filter rows using a condition,
- save cleaned data as a new CSV file.

## 1. Prepare the Conda environment

Open a terminal in this folder and activate the environment from Module 1:

```bash
conda activate scientific-basics
conda install pandas
```

If you prefer Mamba:

```bash
mamba activate scientific-basics
mamba install pandas
```

Check that pandas is installed:

```bash
python -c "import pandas; print(pandas.__version__)"
```

## 2. Run the module

1. Open `02_reading_csv_data.py` in VS Code.
2. Select the `scientific-basics` Conda environment.
3. Keep `02_reading_csv_data.csv` in the same folder as the Python file.
4. Run the cells from top to bottom with **Run Cell** or `Shift+Enter`.

You can also run the entire module:

```bash
conda activate scientific-basics
python 02_reading_csv_data.py
```

The script creates `02_reading_csv_data_cleaned.csv`. This is a new file; the
original data file is not changed.

## 3. Follow the data step by step

### Read the file

```python
data = pd.read_csv("02_reading_csv_data.csv")
```

The result is a pandas **DataFrame**, which is a table with named columns.

### Inspect the table

The `shape` property reports `(rows, columns)`. The `isna()` operation finds
missing values.

```python
print(data.shape)
print(data.isna().sum())
```

The example contains one missing temperature on day 3.

### Fill a missing value

```python
data["temperature_c"] = data["temperature_c"].interpolate()
```

Interpolation estimates the missing value using nearby values. For these
measurements, pandas estimates a temperature between day 2 and day 4.

### Ask questions with filters

```python
warm_days = data[data["temperature_c"] > 20]
```

This keeps only rows where the temperature is greater than 20 °C.

## 4. Copy-and-paste practice

Try these changes one at a time:

1. Add a sixth row to the CSV file.
2. Change the warm-day threshold from `20` to `21`.
3. Calculate the average rainfall with
   `data["rainfall_mm"].mean()`.
4. Print only rainy days with
   `data[data["rainfall_mm"] > 0]`.
5. Add a second line to the plot for `rainfall_mm`.
6. Replace the blank temperature in the CSV file with a number and compare
   the output.

## 5. Common beginner errors

- **`FileNotFoundError`**: open the terminal in the module folder, or use the
  full path to the CSV file.
- **`ModuleNotFoundError: No module named 'pandas'`**: activate
  `scientific-basics` and run `conda install pandas`.
- **The output still shows a blank value**: run the cleaning cell before the
  summary and filtering cells.
- **The cleaned file is missing**: the final cell must run successfully.

## Next module

The next step is to compare two datasets, such as measurements from two
locations, and plot them on the same figure.
