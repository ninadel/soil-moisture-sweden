import os
import pandas as pd

input_dir = r"C:\git\soil-moisture-sweden\test_input_data\20200803222312 SMAP L4 ERA5 0-1 absolute - Copy"
output_dir = r"C:\git\soil-moisture-sweden\test_output_data"
print(os.listdir(input_dir))

merged_metrics = None
for filename in os.listdir(input_dir):
    file = os.path.join(input_dir, filename)
    df = pd.read_csv(file)
    if merged_metrics is None:
        merged_metrics = df
    else:
        merged_metrics = pd.concat([merged_metrics, df])

print(merged_metrics)
print(merged_metrics.columns)
merged_metrics.to_csv(os.path.join(output_dir, "20200803222312 SMAP L4 ERA5 0-1 absolute merged metrics.csv"))