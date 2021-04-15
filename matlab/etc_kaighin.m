path = 'C:\git\soil-moisture-sweden\analysis_output\tc_analysis_20210314104637\matched_data'
result_path = 'C:\git\soil-moisture-sweden\analysis_output\tc_analysis_20210314104637'
files = dir(strcat(path,'\*.csv'))
L = length (files);
result_matrix = []
% disp(path)

for i=1:L
    fparts = split(files(i).name, "_");
    loc = split(fparts(length(fparts)), ".");
    loc = strrep(loc,".csv", "");
    loc = loc(1);
    %     fparts = split(split(files(i).name, ".")(1), "_");
%     disp(strcat(path,'\',files(i).name))
    t = readtable(strcat(path,'\',files(i).name));
    
    % get product names from columns
    prod1 = t.Properties.VariableNames(2);
    prod2 = t.Properties.VariableNames(3);
    prod3 = t.Properties.VariableNames(4);

    rho2_1 = NaN;
    rho2_2 = NaN;
    rho2_3 = NaN;

    errvar_1 = NaN;
    errvar_2 = NaN;
    errvar_3 = NaN;

    if height(t) > 1
        % isolate columns in array
        a = t(:,2:4);
        % convert table to matrix
        a = a{:,:};
        
        % kaighin
        Q_hat = cov(a);

        rho_ETC = [sqrt(Q_hat(1,2)*Q_hat(1,3)/Q_hat(1,1)/Q_hat(2,3)); ...
                sign(Q_hat(1,3)*Q_hat(2,3))*sqrt(Q_hat(1,2)*Q_hat(2,3)/Q_hat(2,2)/Q_hat(1,3)); ...
                sign(Q_hat(1,2)*Q_hat(2,3))*sqrt(Q_hat(1,3)*Q_hat(2,3)/Q_hat(3,3)/Q_hat(1,2))];

        rho2_ETC = rho_ETC.^2;

        errVar_ETC = [(Q_hat(1,1) - Q_hat(1,2)*Q_hat(1,3)/Q_hat(2,3)); ...
                (Q_hat(2,2) - Q_hat(1,2)*Q_hat(2,3)/Q_hat(1,3)); ...
                (Q_hat(3,3) - Q_hat(1,3)*Q_hat(2,3)/Q_hat(1,2))];

        rho2_1 = rho2_ETC(1);
        rho2_2 = rho2_ETC(2);
        rho2_3 = rho2_ETC(3);

        errvar_1 = errVar_ETC(1);
        errvar_2 = errVar_ETC(2);
        errvar_3 = errVar_ETC(3);
    end

    result_matrix = [result_matrix; loc, prod1, prod2, prod3, rho2_1, rho2_2, rho2_3, errvar_1, errvar_2, errvar_3];
    result_table = array2table(result_matrix);
    result_table.Properties.VariableNames(1:10) = ["loc", "prod1", "prod2", "prod3", "rho2_1", "rho2_2", "rho2_3", "errvar_1", "errvar_2", "errvar_3"];
    writetable(result_table, strcat(result_path,'\',"tc_matlab_results.csv"));

end