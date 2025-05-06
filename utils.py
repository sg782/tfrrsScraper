import numpy as np

def get_rolling_avg_n(data, n):
    out = []

    for i in range(len(data)):
        running_n = min(i,n)

        out.append(np.mean(data[i-running_n:i]))

    return out
