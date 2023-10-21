function [theta2, b] = calculateTheta2AndB(theta1, theta3, c)
    % �����ṩ�Ĺ�ʽ����theta2��b

    c_1 = c*sind(180-theta3);
    a_1 = 0.1*sind(theta1);
    c_2 = c*cosd(180-theta3);
    a_2 = 0.1*cosd(theta1);
    % ����theta2
    theta2 = atand((c_1-a_1) /(1-c_2-a_2));
    % ����b
    b = (c_1-a_1) / sind(theta2);

end
