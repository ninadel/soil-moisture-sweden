path = 'C:\git\soil-moisture-sweden\analysis_output\tc_analysis_20210314104637\matched_data'
files = dir(strcat(path,'\*.csv'))
L = length (files);
datasave = []

for i=1:L
    t = readtable(strcat(path,'\',files(i).name));
    a = table2array(t(:, 2:4))
    datasave = [datasave; i];
end