t = readtable(f);
X = table2array(t(:,2)); Y = table2array(t(:,3)); Z = table2array(t(:,4));
% isolate columns in array
y = t(:,2:4);
% convert table to matrix
y = y{:,:}

% grey nearing
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
sX_a = sX/Qxx;
sY_a = sY/Qyy;
sZ_a = sZ/Qzz;

% s = variance, or RMSE squared
rmse_X = sqrt(sX);
rmse_Y = sqrt(sY);
rmse_sZ = sqrt(sZ);


% r = rho? correlation coefficients?
rX = Qxy*Qxz/Qxx/Qyz;
rY = Qxy*Qyz/Qyy/Qxz;
rZ = Qxz*Qyz/Qzz/Qxy;

% kaighin
Q_hat = cov(y);

rho_ETC = [sqrt(Q_hat(1,2)*Q_hat(1,3)/Q_hat(1,1)/Q_hat(2,3)); ...
        sign(Q_hat(1,3)*Q_hat(2,3))*sqrt(Q_hat(1,2)*Q_hat(2,3)/Q_hat(2,2)/Q_hat(1,3)); ...
        sign(Q_hat(1,2)*Q_hat(2,3))*sqrt(Q_hat(1,3)*Q_hat(2,3)/Q_hat(3,3)/Q_hat(1,2))];

rho2_ETC = rho_ETC.^2;
    
errVar_ETC = [(Q_hat(1,1) - Q_hat(1,2)*Q_hat(1,3)/Q_hat(2,3)); ...
        (Q_hat(2,2) - Q_hat(1,2)*Q_hat(2,3)/Q_hat(1,3)); ...
        (Q_hat(3,3) - Q_hat(1,3)*Q_hat(2,3)/Q_hat(1,2))];