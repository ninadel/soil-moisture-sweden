import os
import pandas as pd

input_dir = r"..\analysis_output\ERA5 0-1 grid evaluation 20200804044015"
output_dir = input_dir

merged_metrics = None
for filename in os.listdir(input_dir):
    if filename[-4::] == ".csv":
        file = os.path.join(input_dir, filename)
        df = pd.read_csv(file)
        if merged_metrics is None:
            merged_metrics = df
        else:
            merged_metrics = pd.concat([merged_metrics, df])

merged_metrics.to_csv(os.path.join(output_dir, "merged metrics.csv"), index=False)