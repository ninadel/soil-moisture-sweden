"""
Author: Nina del Rosario
Date: UPDATE_DATE
UPDATE_DESCRIPTION
"""

import os
import pandas as pd

input_dir = r"..\analysis_output\ERA5 0-1 grid evaluation 20200804182046\all_metrics"
# "C:\git\soil-moisture-sweden\analysis_output\station evaluation 20200818002200\network_metrics"
output_dir = r"..\analysis_output\ERA5 0-1 grid evaluation 20200804182046"

merged_metrics = None
for filename in os.listdir(input_dir):
    if filename[-4::] == ".csv":
        file = os.path.join(input_dir, filename)
        df = pd.read_csv(file)
        if merged_metrics is None:
            merged_metrics = df
        else:
            merged_metrics = pd.concat([merged_metrics, df])

merged_metrics.to_csv(os.path.join(output_dir, "grid_metrics.csv"), index=False)
