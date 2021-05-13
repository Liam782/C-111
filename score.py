import csv
import pandas as pd
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random

df = pd.read_csv("score.csv")
data = df["Math_score"].tolist()

#fig = ff.create_distplot([data], ["Math scores"], show_hist = False)
#fig.show()

mean = statistics.mean(data)
std_deviation = statistics.stdev(data)

print("The mean is {} and the standard deviation is {}".format(mean, std_deviation))