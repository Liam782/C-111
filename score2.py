import csv
import pandas as pd
import plotly.figure_factory as ff 
import plotly.graph_objects as go 
import statistics
import random

df = pd.read_csv("score.csv")
data = df["Math_score"].tolist()

fig = ff.create_distplot([data], ["Math scores"], show_hist = False)
fig.show()

def random_set_of_mean(counter):
    dataset = []

    for i in range(0,counter):
        random_index = random.randint(0,len(data) - 1)
        value = data[random_index]
        dataset.append(value)

    mean = statistics.mean(dataset)
    return mean

mean_list = []

for i in range(0,1000):
    set_of_means = random_set_of_mean(100)
    mean_list.append(set_of_means)

std_deviation = statistics.stdev(mean_list)
mean = statistics.mean(mean_list)

print("mean of the sampling distribution is: ", mean)

fig = ff.create_distplot([mean_list], ["Student marks"], show_hist = False)
fig.add_trace[go.Scatter(x = [mean,mean], y = [0,0.20], mode = "lines", name = "Mean")]
fig.show()

#mean = statistics.mean(data)
#std_deviation = statistics.stdev(data)

#print("The mean is {} and the standard deviation is {}".format(mean, std_deviation))