clear; close all; clc;

%% Parameters
% Bars
l_1 = 0.1;                      % Length bar l1
l_0 = 1;                        % Length bar l0 (fixed)
l_3 = 0.8956;       % Length bar l3

% Given angles
theta1 = 144.0089;  % Replace with the known value for theta1
theta3 = 19.9744;               % Replace with the known value for theta3

% Bar l3 end coordinates (based on theta3)
x3 = l_0 + l_3 * cosd(theta3);
y3 = l_3 * sind(theta3);

% Bar l1 end coordinates (based on theta1)
x1 = l_1 * cosd(theta1);
y1 = l_1 * sind(theta1);

% Compute l2 length using distance formula
l_2 = sqrt((x3 - x1)^2 + (y3 - y1)^2);

% Calculate theta2 using atan2
theta2 = atan2(y3 - y1, x3 - x1);
theta2_deg = rad2deg(theta2);

disp(['The length of l2 is: ', num2str(l_2), ' meters.']);
disp(['The angle theta2 (between l2 and the x-axis) is: ', num2str(theta2_deg), ' degrees.']);

%% Display linkage
figure
hold on; grid on; axis equal
title('Four-bar linkage shape for given angles')
% Plot bars
plot([0, l_0], [0, 0], 'k', 'LineWidth', 2); % Fixed bar l0
plot([0, x1], [0, y1], 'b', 'LineWidth', 2); % Bar l1
plot([x1, x3], [y1, y3], 'r', 'LineWidth', 2); % Bar l2
plot([l_0, x3], [0, y3], 'g', 'LineWidth', 2); % Bar l3

% Plot joints
plot(0, 0, 'ko', 'MarkerFaceColor', 'k'); % O joint
plot(l_0, 0, 'ko', 'MarkerFaceColor', 'k'); % O' joint
plot(x1, y1, 'ko', 'MarkerFaceColor', 'k'); % A joint
plot(x3, y3, 'ko', 'MarkerFaceColor', 'k'); % B joint

xlabel('X'); ylabel('Y');
legend('Fixed bar l0', 'Bar l1', 'Bar l2', 'Bar l3', 'Location', 'Best');

