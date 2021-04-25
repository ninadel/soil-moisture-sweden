import os
import re
import sm_tools as tools


def export_matched(triplet_subdir, input_dir, output_root, anomaly=True):
    #     result_str = re.findall(date_search_str, filename)[-1]
    for filename in os.listdir(triplet_subdir[0]):
        # result_str = re.findall(date_search_str, filename)[-1]
        loc_str = re.findall(r"[0-9]{6}", filename)[-1]
        triplet_files = [(dataset, os.path.join(input_dir, dataset, "{}_{}.csv".format(dataset, loc_str)))
                         for dataset in triplet]
        matched_data, match_str = tools.temporal_match_csv(triplet_files, loc_str, anomaly=anomaly)
        matched_subdir = os.path.join(output_root, "matched_data")
        if not os.path.exists(matched_subdir):
            os.makedirs(matched_subdir)
        output_file = os.path.join(matched_subdir, "matched_{}.csv".format(match_str))
        matched_data.to_csv(output_file)

# input_dir = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT"
# output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC1_IncludeASCAT"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\SMAP L3 Enhanced"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\ASCAT 12.5 TS"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\ERA5 0-1"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\SMOS-IC"

# triplet = ['SMAP L3 Enhanced', 'ASCAT 12.5 TS', 'ERA5 0-1']
# triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
#
# export_matched(triplet_subdir, input_dir, output_root)
#
# triplet = ['SMOS-IC', 'ASCAT 12.5 TS', 'ERA5 0-1']
# triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
#
# export_matched(triplet_subdir, input_dir, output_root)
#
# input_dir = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC2_ExcludeASCAT"
# output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC2_ExcludeASCAT"
#
# triplet = ['SMOS-IC', 'Sentinel-1', 'ERA5 0-1']
# triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
# export_matched(triplet_subdir, input_dir, output_root)
#
# triplet = ['SMAP L3 Enhanced', 'Sentinel-1', 'ERA5 0-1']
# triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
# export_matched(triplet_subdir, input_dir, output_root)

input_dir = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC2_ExcludeASCAT"
output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC2_AbsoluteExcludeASCAT"
sentinel = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC2_ExcludeASCAT\Sentinel-1"
temp_input_dir = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC3_AbsoluteExcludeASCAT"

for filename in os.listdir(sentinel):
    file = os.path.join(sentinel, filename)
    df = tools.csv_to_pdseries(file)
    df = df/100
    if not os.path.exists(temp_input_dir):
        os.makedirs(temp_input_dir)
    df.to_csv(os.path.join(temp_input_dir, filename))


input_dir = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC3_AbsoluteExcludeASCAT"


output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC3_AbsoluteExcludeASCAT"

# absolute
triplet = ['SMOS-IC', 'Sentinel-1', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
export_matched(triplet_subdir, input_dir, output_root, anomaly=False)

output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC4_AbsoluteExcludeASCAT"

triplet = ['SMAP L3 Enhanced', 'Sentinel-1', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
export_matched(triplet_subdir, input_dir, output_root, anomaly=False)

output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC5_AnomalyeExcludeASCAT"

triplet = ['SMAP L3 Enhanced', 'Sentinel-1', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
export_matched(triplet_subdir, input_dir, output_root, anomaly=True)

output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC6_AnomalyeExcludeASCAT"

triplet = ['SMOS-IC', 'Sentinel-1', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
export_matched(triplet_subdir, input_dir, output_root, anomaly=True)
