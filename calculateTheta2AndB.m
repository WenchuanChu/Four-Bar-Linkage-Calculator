function [theta2, b] = calculateTheta2AndB(theta1, theta3, c)
    % 根据提供的公式计算theta2和b

    c_1 = c*sind(180-theta3);
    a_1 = 0.1*sind(theta1);
    c_2 = c*cosd(180-theta3);
    a_2 = 0.1*cosd(theta1);
    % 计算theta2
    theta2 = atand((c_1-a_1) /(1-c_2-a_2));

    % 计算b
    b = (c_1-a_1) / sind(theta2);

end
