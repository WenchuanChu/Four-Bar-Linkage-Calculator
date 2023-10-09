function objective = func_to_minimize(x)
    % Extracting variables from input vector x
    theta1 = x(1);
    theta3 = x(2);
    c = x(3);
    
    theta1_case1 = theta1+30;
    theta1_case2 = theta1-30;
    theta3_case1 = theta3+7;
    theta3_case2 = theta3-20;
    
    [theta2, b] = calculateTheta2AndB(theta1, theta3, c);
    [theta2_case1, b_case1] = calculateTheta2AndB(theta1_case1, theta3_case1, c);
    [theta2_case2, b_case2] = calculateTheta2AndB(theta1_case2, theta3_case2, c);
    
    
    
    % Defining the six equations
    eq1 = 0.1*cosd(theta1) + b*cosd(theta2) - c*cosd(theta3)-1;
    eq2 = 0.1*sind(theta1) + b*sind(theta2) - c*sind(theta3);
    eq3 = 0.1*cosd(theta1_case1) + b*cosd(theta2_case1) - c*cosd(theta3_case1)-1;
    eq4 = 0.1*sind(theta1_case1) + b*sind(theta2_case1) - c*sind(theta3_case1);
    eq5 = 0.1*cosd(theta1_case2) + b*cosd(theta2_case2) - c*cosd(theta3_case2)-1;
    eq6 = 0.1*sind(theta1_case2) + b*sind(theta2_case2) - c*sind(theta3_case2);
    
    eq7 = theta1 + (180-theta1+theta2) + (180-theta3) + (theta3 - theta2)-360;
    %case1
    eq8 = (theta1_case1) + (180- theta1_case1 + theta2_case1) + (180-theta3_case1) + (theta3_case1 - theta2_case1)-360;
    %case2
    eq9 = (theta1_case2) + (180- theta1_case2 + theta2_case2) + (180-theta3_case2) + (theta3_case2 - theta2_case2)-360;

    % Objective function: sum of absolute values of all equations
    objective = abs(eq1) + abs(eq2) + abs(eq3) + abs(eq4) + abs(eq5) + abs(eq6) + abs(eq7) + abs(eq8) + abs(eq9);
end