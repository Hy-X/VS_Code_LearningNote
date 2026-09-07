# Plot Wave in Jupyter Notebook

This project fetches and plots seismic waveform data using [ObsPy](https://docs.obspy.org/), styled with `matplotlib`/`seaborn`. It's written as a plain `.py` script using VS Code's **Python Interactive Window** cell syntax instead of a `.ipynb` notebook file.

## Requirements

### 0. Python itself

You need Python 3.9+ installed on your computer first. Check by running `python3 --version` in a terminal. If that fails, install Python from [python.org](https://www.python.org/downloads/) before continuing.

### 1. VS Code extensions

Open the **Extensions** view in VS Code (`Cmd+Shift+X` on macOS, `Ctrl+Shift+X` on Windows/Linux), search for each name below, and click **Install**:

- **Python** (publisher: Microsoft) — provides the `# %%` cell CodeLens and kernel selection.
- **Jupyter** (publisher: Microsoft) — powers the Interactive Window that cells run in (usually installed automatically as a dependency of the Python extension).

### 2. Python packages

- `obspy` — fetches and processes seismic waveform data via FDSN web services.
- `matplotlib` — underlying plotting engine used by ObsPy and for figure styling.
- `seaborn` — theming (grid, palette, fonts) applied on top of matplotlib.
- `ipykernel` — required for the Interactive Window to run cells against a Jupyter kernel.

Open a terminal in this project folder and run:

```bash
pip install obspy matplotlib seaborn ipykernel
```

> Tip: if you have multiple Python versions, use `pip3` instead of `pip`, or create a virtual environment first (`python3 -m venv .venv && source .venv/bin/activate`).

## The `# %%` cell workflow

VS Code's Python extension recognizes the comment marker `# %%` as a **cell delimiter**. Any code between two `# %%` markers is treated as one executable cell, similar to a Jupyter notebook cell — but the code lives in an ordinary `.py` file.

```python
# %%
import obspy
# this is cell 1

# %%
st = obspy.read()
# this is cell 2
```

### How it works with the Interactive Window

- When you open a `.py` file containing `# %%` markers, VS Code shows a **"Run Cell"** CodeLens link above each cell.
- Clicking **Run Cell** (or placing the cursor in a cell and pressing `Shift+Enter`) sends just that cell's code to the **Python Interactive Window**, a Jupyter kernel-backed panel that runs alongside your editor.
- Variables, imports, and state persist in the kernel between cell runs, so later cells (e.g. the plotting cell) can reuse objects created in earlier cells (e.g. the `st` stream fetched from IRIS).
- Rich outputs — such as `matplotlib`/`seaborn` figures from `fig.show()` or `plt.show()` — render inline in the Interactive Window panel, just like in a notebook.
- Because the file stays a `.py` script, it's easy to diff, lint, and version-control with git, while still getting notebook-like interactivity.

### Running this script

1. Open `obspy_show_waveform.py` in VS Code.
2. In the top-right corner of the editor, click **Select Kernel** and choose the Python environment where you installed the packages above.
3. Run each `# %%` cell from top to bottom, either by clicking **Run Cell** above the cell or by placing your cursor in the cell and pressing `Shift+Enter`:
   - **Cell 1** — imports and status message.
   - **Cell 2** — connects to the IRIS FDSN client and downloads the past hour of waveform data for station `FNO`.
   - **Cell 3** — demeans, detrends, and bandpass-filters the stream.
   - **Cell 4** — applies a Nature-publication-style theme and plots the waveform.
4. A new **Interactive Window** panel opens next to your editor showing the printed stream info and the plot.

### Troubleshooting

- **"No kernel selected" or the Run Cell buttons don't appear**: make sure both the Python and Jupyter extensions are installed and enabled, then reopen the file.
- **`ModuleNotFoundError: No module named 'obspy'`**: the packages weren't installed into the environment you selected as the kernel — re-run the `pip install` command using that environment's `pip`, or reselect the kernel to match where you installed them.
- **No waveform data / empty stream**: station `FNO` may not have data for the requested time window on IRIS. Try a different, well-known station/network or widen the time range in Cell 2.

### More `# %%` tips

- **Run all cells**: use the **Run All Cells** CodeLens at the top of the file, or the Command Palette (`Cmd+Shift+P` / `Ctrl+Shift+P`) → "Jupyter: Run All Cells".
- **Run everything above/below**: right-click in a cell, or use the CodeLens links "Run Above"/"Run Below", to replay earlier cells without re-running the whole file.
- **Variables panel**: while the Interactive Window is open, click **Variables** in its toolbar to inspect live objects (e.g. `st`, `fig`) like you would in a notebook's variable explorer.
- **Debugging a cell**: use the "Debug Cell" CodeLens to step through a single cell with breakpoints, instead of debugging the whole script.
- **Restarting state**: if variables get into a confusing state, use the "Restart Kernel" button in the Interactive Window toolbar to start fresh, then re-run cells from the top.
- **Converting to a notebook**: the Command Palette action "Jupyter: Export Current Python File as Jupyter Notebook" turns this `.py` file into a `.ipynb` file with the same cells, if you ever need the notebook format.
- Official docs: [Jupyter support in VS Code — Python interactive window](https://code.visualstudio.com/docs/python/jupyter-support-py).
