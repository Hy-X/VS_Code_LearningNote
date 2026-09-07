# %% Imports
import matplotlib.pyplot as plt
import seaborn as sns
from obspy import UTCDateTime
from obspy.clients.fdsn import Client

# %%

print ("Initializing ObsPy and setting up the client...")

# %% Fetch the past hour of waveform data for station FNO from IRIS
client = Client("IRIS")

# wildcards let get_waveforms match FNO regardless of network/location/channel code
network = "*"
station = "FNO"
location = "*"
channel = "*"

endtime = UTCDateTime.now()
starttime = endtime - 3600  # past hour

st = client.get_waveforms(
    network=network,
    station=station,
    location=location,
    channel=channel,
    starttime=starttime,
    endtime=endtime,
)
print(st)

# %% Remove offset/drift and isolate the 1-10 Hz band before plotting
st.detrend("demean")
st.detrend("linear")
st.filter("bandpass", freqmin=1.0, freqmax=10.0, corners=4, zerophase=True)

# %% Plot with a style theme (white background, light grid, sans-serif)
sns.set_theme(style="whitegrid", palette="deep", context="paper")
plt.rcParams.update({
    "font.family": "sans-serif",
    "font.sans-serif": ["Arial", "Helvetica", "DejaVu Sans"],
    "axes.linewidth": 0.8,
    "grid.linewidth": 0.5,
    "grid.color": "0.85",
})

fig = st.plot(color="steelblue", linewidth=0.8, handle=True, show=False)
fig.suptitle(f"Station {station} — Waveform (past hour)", fontsize=14, fontweight="bold")

for ax in fig.axes:
    ax.set_ylabel(ax.get_ylabel(), fontsize=10)
    ax.set_xlabel("Time (UTC)", fontsize=10)
    ax.tick_params(labelsize=8)
    ax.grid(True, linewidth=0.5, color="0.85")
    ax.set_axisbelow(True)
    sns.despine(ax=ax)

fig.tight_layout()
plt.show()

