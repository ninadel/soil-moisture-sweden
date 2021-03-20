function [sX,sY,sZ,rX,rY,rZ] = matlab_graynearing_triple_collocation(X,Y,Z)
% source: https://github.com/grey-nearing/triple_collocation/blob/master/tools/triple_collocation.m

% Q = covariance matrix?
Qxx = cov(X,X); Qxx = Qxx(2);
Qyy = cov(Y,Y); Qyy = Qyy(2);
Qzz = cov(Z,Z); Qzz = Qzz(2);

Qxy = cov(X,Y); Qxy = Qxy(2);
Qxz = cov(X,Z); Qxz = Qxz(2);
Qyz = cov(Y,Z); Qyz = Qyz(2);

% s = variance, or RMSE squared
sX = Qxx - Qxy*Qxz/Qyz;
sY = Qyy - Qxy*Qyz/Qxz;
sZ = Qzz - Qxz*Qyz/Qxy;

% s = what is this?
sX = sX/Qxx;
sY = sY/Qyy;
sZ = sZ/Qzz;

% r = rho? correlation coefficients?
rX = Qxy*Qxz/Qxx/Qyz;
rY = Qxy*Qyz/Qyy/Qxz;
rZ = Qxz*Qyz/Qzz/Qxy;
end

% "C:\Users\neene\Documents\LuDrive\academic\Lund\GISM01\Soil moisture thesis\scripting research\testtcdata_matched_ERA5 0-1_ASCAT 12.5 TS_SMAP L3 Enhanced_anomaly_863351.csv"
% T = readtable('testtcdata_matched_ERA5 0-1_ASCAT 12.5 TS_SMAP L3 Enhanced_anomaly_863351.csv');