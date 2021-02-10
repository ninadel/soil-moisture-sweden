from pytesmo.metrics import tcol_snr
import numpy as np
import pandas as pd
import sm_tools as tools

# runs fine
f = r"..\analysis_output\tc_analysis_troubleshoot\tc_analysis_20200907211403\matched_data\matched_ERA5 0-1_ASCAT 12.5 TS_SMAP L3 Enhanced_anomaly_907993.csv"
# # returns error
# f = r"..\analysis_output\tc_analysis_troubleshoot\tc_analysis_20200907211403\matched_data\matched_ERA5 0-1_ASCAT 12.5 TS_SMOS-IC_anomaly_907993.csv"
loc = (f.split(".")[-2]).split("_")[-1]
print(loc)
matched_data = pd.read_csv(f)
triplet = matched_data.columns[1::]
print(triplet)
x, y, z = matched_data[triplet[0]].to_numpy(), matched_data[triplet[1]].to_numpy(), matched_data[triplet[2]].to_numpy()
# print(products)
#
# print(df.loc[:,products[0]])
# print(df.loc[:,products[1]])
# print(df.loc[:,products[2]])

# snr, err_std, beta = tcol_snr(x, y, z)

n = matched_data.shape[0]
print('{} {} n: {}'.format(loc, triplet, n))
# print('{} {} snr: {}'.format(loc, triplet, snr))
# print('{} {} err_std: {}'.format(loc, triplet, err_std))
# print('{} {} beta: {}'.format(loc, triplet, beta))

cov = np.cov(np.vstack((x, y, z)))
print(cov)
ind = (0, 1, 2, 0, 1, 2)
ref_ind = 0
no_ref_ind = np.where(np.arange(3) != ref_ind)[0]

i = 0
print(cov[0,0])
# # TUW-GEO error?
# snr = 10 * np.log10(
#     [((cov[i, i] * cov[ind[i + 1], ind[i + 2]]) / (cov[i, ind[i + 1]] * cov[i, ind[i + 2]]) - 1) ** (-1)])
# fixed??
snr = (-10) * np.log10(
    [((cov[i, i] * cov[ind[i + 1], ind[i + 2]]) / (cov[i, ind[i + 1]] * cov[i, ind[i + 2]]) - 1)])
print(snr)
    # for i in np.arange(3)])
test0 = [((cov[i, i] * cov[ind[i + 1], ind[i + 2]]) / (cov[i, ind[i + 1]] * cov[i, ind[i + 2]]) - 1)]
print(test0)

test1 = [((cov[i, i] * cov[ind[i + 1], ind[i + 2]]) / (cov[i, ind[i + 1]] * cov[i, ind[i + 2]]) - 1) ** (-1)]
print(test1)
#
test2 = cov[0, 0]
print(test2)
print(np.var(x))
# test2 = cov[0]
# snr = 10 * np.log10(test)

# SNR_x =

snr, err_std, beta = tcol_snr(matched_data[triplet[0]].to_numpy(),
                                         matched_data[triplet[1]].to_numpy(),
                                         matched_data[triplet[2]].to_numpy())
print("hi")
print('{} {} snr: {}'.format(loc, triplet, snr))
print('{} {} err_std: {}'.format(loc, triplet, err_std))
print('{} {} beta: {}'.format(loc, triplet, beta))

snr, err_std, beta = tools.calc_tcol_snr(matched_data[triplet[0]].to_numpy(),
                                         matched_data[triplet[1]].to_numpy(),
                                         matched_data[triplet[2]].to_numpy())
print("hi again")
print('{} {} snr: {}'.format(loc, triplet, snr))
print('{} {} err_std: {}'.format(loc, triplet, err_std))
print('{} {} beta: {}'.format(loc, triplet, beta))
