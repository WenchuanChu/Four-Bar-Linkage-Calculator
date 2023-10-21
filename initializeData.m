% The order of variable:
% [theta1],[theta2],[theta3],[theta4],[delta_theta1],[delta_theta2],[delta_theta3],[delta_theta4]
% [a],[b],[c],[d]

function [thetaData, lengthData] = initializeData()
    % Initialize theta related data
    thetaData.theta1 = 0;
    thetaData.theta2 = 0;
    thetaData.theta3 = 0;
    thetaData.theta4 = 0;
    thetaData.delta_theta1_case1 = 30;
    thetaData.delta_theta2_case1 = 0;
    thetaData.delta_theta3_case1 = 7;
    thetaData.delta_theta4_case1 = 0;
    thetaData.delta_theta1_case2 = -30;
    thetaData.delta_theta2_case2 = 0;
    thetaData.delta_theta3_case2 = -20;
    thetaData.delta_theta4_case2 = 0;

    % Initialize [a, b, c, d] data
    lengthData.a = 0.1;
    lengthData.b = 0;
    lengthData.c = 0;
    lengthData.d = 1;
end
