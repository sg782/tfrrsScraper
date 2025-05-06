import numpy as np
import matplotlib.pyplot as plt

def get_rolling_avg_n(data, n):
    out = []

    for i in range(len(data)):
        running_n = min(i,n)

        out.append(np.mean(data[i-running_n:i]))

    return out


def plot_event_data(event, data):
    pass

def clean_pv_data(heights):
    for i in range(len(heights)):
        height = heights[i]

        height = height.replace("m", "")
        if height == "NH":
            height= 0.0

        heights[i] = float(height)

    return heights


