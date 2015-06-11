import plotly.plotly as py
from plotly.graph_objs import *
import time


trace1 = Scatter(
        x=[],
        y=[],
        stream=dict(token='stream_token')
    )
data = Data([trace1])
py.plot(data)
s = py.Stream('stream_token')


def sleepcycle():

    time_hhmmss = time.strftime("%H:%M:%S")
    date_mmddyyyy = time.strftime("%m/%d/%Y")
    dtstamp = date_mmddyyyy + ' ' + time_hhmmss
    s.open()
    s.write(dict(x=dtstamp, y=400))
    s.close()
    time.sleep(10)

while True:
    sleepcycle()
