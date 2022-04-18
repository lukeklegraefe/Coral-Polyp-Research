import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

'''
Set 'splice' to determine how large of a frame interval to calculate for standard deviation,
average polyps, and for error bar visual clarity.
'''

data = 'EASY.csv'
df = pd.read_csv(data)

frame_col = df['Frame']
splice = 20
count = [0] * (frame_col.max() + 1)

snr = []
snr_max = []
snr_min = []

snr_diff_min = []
snr_diff_max = []

total_polyps = 0

for idx, val in enumerate(frame_col):
    count[val] += 1

total_polyps = np.sum(count)
splicedArr = [0] * splice
reset = 0

for idx, val in enumerate(count):
    if val > 6:
        if reset >= splice:
            snr_max.append(np.max(splicedArr))
            snr_min.append(np.min(splicedArr))
            snr_diff_max.append(np.max(splicedArr) - np.average(splicedArr))
            snr_diff_min.append(np.average(splicedArr) - np.min(splicedArr))
            reset = 0
            print("Average (ID ", idx, "): ", np.average(splicedArr))
            snr.append(np.average(splicedArr))
        splicedArr[reset] = val
        reset += 1

errors = [[len(snr)]*2 for i in range(2)]
errors[0] = snr_diff_min
errors[1] = snr_diff_max

plt.errorbar(np.linspace(0, len(snr)*splice, len(snr)), snr, errors, color='green', fmt='-o', elinewidth=1)
plt.title("Error Bar with Segment Size = " + str(splice))
plt.xlabel("Frame")
plt.ylabel("# of Polyps Identified")
plt.show()

total_polyps = np.sum(snr) * splice
avg_polyps = np.average(snr)
print("Total polyps counted: " + str(total_polyps) + "\nAverage polyps per frame: " + str(avg_polyps))
print("Average: ", np.average(snr), " from ", len(snr), " total splices")
print("Standard deviation: ", np.std(snr))
