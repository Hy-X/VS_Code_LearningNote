# Scientific Computing Basics: First Steps

This lesson is a gentle first step into scientific computing with Python. You
will create a small temperature dataset, calculate useful values, and make a
plot. The examples are short enough to copy and run one cell at a time.

You do not need to know advanced mathematics or Python before starting.

## What you will learn

By the end of this lesson, you will be able to:

- store measurements in a NumPy array,
- calculate a mean, minimum, maximum, and standard deviation,
- write a small function,
- make a simple line plot,
- change an example to answer your own question.

## 1. Create a Conda environment

This lesson uses the same environment workflow introduced in the Conda
tutorial. Open a terminal and create a named environment:

```bash
conda create -n scientific-basics python=3.11 numpy matplotlib
```

Activate it:

```bash
conda activate scientific-basics
```

Check that the environment is active and the packages are available:

```bash
python --version
python -c "import numpy, matplotlib; print('Packages are ready!')"
```

If your class uses Mamba, the equivalent commands are:

```bash
mamba create -n scientific-basics python=3.11 numpy matplotlib
mamba activate scientific-basics
```

> Tip: Run `conda activate scientific-basics` whenever you return to this
> lesson. Run `conda env list` if you want to see all your environments.

## 2. Run the lesson in VS Code

1. Install the **Python** extension from Microsoft.
2. Open `01_first_steps.py`.
3. Select the `scientific-basics` Conda environment as the Python interpreter.
4. Run each cell from top to bottom using **Run Cell** or `Shift+Enter`.

The file is an ordinary Python script. The `# %%` lines divide it into small
cells so beginners can run and inspect one idea at a time.

You can also run the complete file from a terminal:

```bash
conda activate scientific-basics
python 01_first_steps.py
```

The final cell opens a plot window. Close the window to let a terminal run
finish.

## 3. What to notice while running

### Measurements are data

The variable `temperatures` is a NumPy array. An array is a convenient
collection of numbers that can be calculated on as a group.

```python
temperatures = np.array([18.5, 19.0, 21.5, 23.0, 22.0])
```

### A result is often a number

`temperatures.mean()` calculates the average. The dot means “use this
operation on this array.”

```python
average = temperatures.mean()
print(average)
```

### A plot helps us see a pattern

The plot uses day numbers on the x-axis and temperatures on the y-axis. Labels
are important: a reader should not have to guess what the numbers mean.

## 4. Copy-and-paste practice

After running the example, try these changes in the practice cell:

1. Replace the five temperatures with measurements from your own week.
2. Change the title to describe your dataset.
3. Add one more day and measurement.
4. Change `threshold = 20` to another value and see which measurements are
   above it.
5. Change the line color from `"steelblue"` to `"darkgreen"`.

Before changing the code, make a copy of the original line so you can compare
the two versions.

## 5. Common beginner errors

- **`ModuleNotFoundError: No module named 'numpy'`**: activate
  `scientific-basics`, then select that same Conda environment in VS Code.
- **`conda: command not found`**: install Miniconda or Anaconda, then open a
  new terminal so Conda is added to your shell.
- **The plot does not appear**: run the cells from top to bottom, or run the
  complete file from a terminal.
- **`NameError`**: a cell that creates the missing variable has not run yet.
- **The numbers look different**: a mean or standard deviation is rounded for
  display, so the stored value can have more decimal places.

## Next lessons

This first lesson is intentionally small. Natural follow-up lessons are:

1. reading a CSV file,
2. cleaning missing measurements,
3. comparing two datasets,
4. fitting a simple model,
5. saving a figure for a report.
