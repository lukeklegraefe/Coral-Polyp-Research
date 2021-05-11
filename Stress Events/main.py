import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb

data = 'AnalyzeParticles_TIGHT.csv'
df = pd.read_csv(data)
df.drop(1, axis=0, inplace=True)
slice_col = df['Slice']
count_col = df['Count']
stress_col = []
stress_idx = []
stress_idx_final = []
total_stress = 0

for idx, val in enumerate(count_col):
    if val == 0:
        print("Stress Event at: ", slice_col[idx])
        stress_col.append(2)
        total_stress += 1
    elif val <= 4:
        print("Stress Event at: ", slice_col[idx])
        stress_col.append(1)
        total_stress += 1
    else:
        stress_col.append(0)

print("\nTotal Length of Stress Events: ", total_stress)
sb.histplot(data=count_col, color='orange')
plt.show()

for idx, val in enumerate(stress_col):
    if idx <= len(stress_col):
        if val > 0:
            if stress_col[idx+1] > 0 or stress_col[idx-1] > 0:
                stress_idx.append(slice_col[idx])
            else:
                stress_col[idx] = 0
                total_stress -= 1

c = 0
for idx, val in enumerate(stress_idx):
    if idx != 0:
        if val == stress_idx[idx-1]+1:
            c += 1
        else:
            print("Consecutive: ", c, " at ", stress_idx[idx-c])
            if c > 30:
                stress_idx_final.append(stress_idx[idx-c])
                stress_idx_final.append(stress_idx[idx-1])
            c = 0

print(stress_idx_final)

print("\nRefined Total Length of Stress Events: ", total_stress)
print("\nIndices of Stress Events: \n", stress_idx)

plt.plot(slice_col, stress_col)
plt.yticks([0, 1, 2])
plt.ylabel("Intensity of Stress")
plt.xlabel("Slice")
plt.show()

output = open("StressEvents.txt", "w")
output.write(', '.join(str(n) for n in stress_idx_final))
output.close()
print("\nSuccessfully written to output.")

