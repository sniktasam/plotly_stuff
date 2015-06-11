import plotly.plotly as py
from plotly.graph_objs import *
import time


trace1 = Scatter(
        x=[],
        y=[],
        stream=dict(token='8zsr23tyti')
    )
data = Data([trace1])
py.plot(data)
s = py.Stream('8zsr23tyti')


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
