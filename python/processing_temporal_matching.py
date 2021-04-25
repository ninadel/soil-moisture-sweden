import os
import re
import sm_tools as tools


def export_matched(triplet_subdir, input_dir, output_root):
    #     result_str = re.findall(date_search_str, filename)[-1]
    for filename in os.listdir(triplet_subdir[0]):
        # result_str = re.findall(date_search_str, filename)[-1]
        loc_str = re.findall(r"[0-9]{6}", filename)[-1]
        triplet_files = [(dataset, os.path.join(input_dir, dataset, "{}_{}.csv".format(dataset, loc_str)))
                         for dataset in triplet]
        matched_data, match_str = tools.temporal_match_csv(triplet_files, loc_str)
        matched_subdir = os.path.join(output_root, "matched_data")
        if not os.path.exists(matched_subdir):
            os.makedirs(matched_subdir)
        output_file = os.path.join(matched_subdir, "matched_{}.csv".format(match_str))
        matched_data.to_csv(output_file)

input_dir = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT"
output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC1_IncludeASCAT"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\SMAP L3 Enhanced"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\ASCAT 12.5 TS"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\ERA5 0-1"
# "C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC1_IncludeASCAT\SMOS-IC"

triplet = ['SMAP L3 Enhanced', 'ASCAT 12.5 TS', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]

export_matched(triplet_subdir, input_dir, output_root)

triplet = ['SMOS-IC', 'ASCAT 12.5 TS', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]

export_matched(triplet_subdir, input_dir, output_root)

input_dir = r"C:\git\soil-moisture-sweden\input_data\resampled_25km_spatial_temporal_match\TC2_ExcludeASCAT"
output_root = r"C:\git\soil-moisture-sweden\analysis_output\matched_data_TC2_ExcludeASCAT"

triplet = ['SMOS-IC', 'Sentinel-1', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
export_matched(triplet_subdir, input_dir, output_root)

triplet = ['SMAP L3 Enhanced', 'Sentinel-1', 'ERA5 0-1']
triplet_subdir = [os.path.join(input_dir, dataset) for dataset in triplet]
export_matched(triplet_subdir, input_dir, output_root)
