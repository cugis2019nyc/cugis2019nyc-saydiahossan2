# -*- coding: utf-8 -*-
"""
Created on Fri Aug 16 07:58:36 2019

@author: columbia
"""

import pandas

import plotly
from plotly. offline import plot
import plotly.graph_objs as go


ccdf = pandas.read_excel("GISdata.xlsx", sheet_name = "cancercases")
ccdf



ccplot = go.Bar(x=ccdf["CancerType"], y=ccdf["Number"],
                marker = {"color": ccdf["Number"],
                            "colorscale" : "Jet"})
plot([ccplot])

titles = go.Layout(title = "Number of Cancer Cases in Women",
                   xaxis=go.layout.XAxis(title=go.layout.xaxis.Title(text = "cancer type",)),
                   yaxis = go.layout.YAxis(title = go.layout.yaxis.Title(text = "Numbers",)
                   )
                   )
                   
fig = go.Figure(data=[ccplot],layout=titles)
plot(fig)
