function F = equations(var)
    % Extracting variables from input vector x
    unknown_theta1 = var(1);
    unknown_theta3 = var(2);
    unknown_c = var(3);
    [thetaValues, lengthValues] = initializeData();
    
    theta1_case1 = unknown_theta1+thetaValues.delta_theta1_case1;
    theta1_case2 = unknown_theta1+thetaValues.delta_theta1_case2;
    theta3_case1 = unknown_theta3+thetaValues.delta_theta3_case1;
    theta3_case2 = unknown_theta3+thetaValues.delta_theta3_case2;
    
    [theta2, b] = calculateTheta2AndB(unknown_theta1, unknown_theta3, unknown_c);
    [theta2_case1] = calculateTheta2AndB(theta1_case1, theta3_case1, unknown_c);
    [theta2_case2] = calculateTheta2AndB(theta1_case2, theta3_case2, unknown_c);
    
    a = lengthValues.a;
    d = lengthValues.d;
    
    
    
    % Defining the six equations
    F(1) = a*cosd(unknown_theta1) + b*cosd(theta2) - unknown_c*cosd(unknown_theta3)-d;
    F(2) = a*sind(unknown_theta1) + b*sind(theta2) - unknown_c*sind(unknown_theta3);
    F(3) = a*cosd(theta1_case1) + b*cosd(theta2_case1) - unknown_c*cosd(theta3_case1)-d;
    F(4) = a*sind(theta1_case1) + b*sind(theta2_case1) - unknown_c*sind(theta3_case1);
    F(5) = a*cosd(theta1_case2) + b*cosd(theta2_case2) - unknown_c*cosd(theta3_case2)-d;
    F(6) = a*sind(theta1_case2) + b*sind(theta2_case2) - unknown_c*sind(theta3_case2);
    
    F(7) = unknown_theta1 + (180-unknown_theta1+theta2) + (180-unknown_theta3) + (unknown_theta3 - theta2)-360;

    F(8) = (theta1_case1) + (180- theta1_case1 + theta2_case1) + (180-theta3_case1) + (theta3_case1 - theta2_case1)-360;

    F(9) = (theta1_case2) + (180- theta1_case2 + theta2_case2) + (180-theta3_case2) + (theta3_case2 - theta2_case2)-360;
    

end