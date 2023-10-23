%% Four-bar linkage
% Compute angle phi for given angle between l_0 and l_1 and display the linkage shape.

clear; close all; clc;

%% Parameters
% Bars
l_1 = 0.1;                      % Length bar a £¨fixed£©                 [m]
l_2 = 1.9385;                  % Length bar b                  [m]
l_3 = 0.8956;                  % Length bar c                  [m]
l_0 = 1;                     % Length bar d£¨fixed£©                  [m]

% Given angle between l_0 and l_1
input_angle = 144.00890-30; % Change this value as per requirement
th = deg2rad(input_angle);


% Definitions
k_1 = -2*l_1*l_3*sin(th);
k_2 = 2*l_3*(l_0-l_1*cos(th));
k_3 = l_0^2 + l_1^2 - l_2^2 + l_3^2 - 2*l_0*l_1*cos(th);



% Compute phi
phi = 2*atan2(-k_1-sqrt(k_1^2+k_2^2-k_3^2),k_3-k_2);
% Convert phi to degrees for display
phi_deg = rad2deg(phi)+360;

if phi_deg>360
    phi_deg = phi_deg - 360;
    if phi_deg > 180
        phi_deg = phi_deg-360;
    end

end


alpha = atan2(-l_1*sin(th)+l_3*sin(phi),l_0-l_1*cos(th)+l_3*cos(phi));
disp(['When theta_1 equals ', num2str(input_angle),' degrees,',' theta_3 is: ', num2str(phi_deg), ' degrees, ','theta_2 is ', num2str(rad2deg(alpha))]);



%%

% Compute linkage coordinates
% Bar 1
bar_1_x = [0, l_1*cos(th)];
bar_1_y = [0, l_1*sin(th)];
% Bar 2

bar_2_x = [l_1*cos(th), l_1*cos(th) + l_2*cos(alpha)];
bar_2_y = [l_1*sin(th), l_1*sin(th) + l_2*sin(alpha)];
% Bar 3
bar_3_x = [l_0, l_0 + l_3*cos(phi)];
bar_3_y = [0, l_3*sin(phi)];




%% Display linkage
figure
hold on; grid on; axis equal
title('Four-bar linkage shape for given angle')
% Plot bars
plot([0, l_0], [0, 0], 'k', 'LineWidth', 2); % Fixed bar
plot(bar_1_x, bar_1_y, 'b', 'LineWidth', 2); % Bar 1
plot(bar_2_x, bar_2_y, 'r', 'LineWidth', 2); % Bar 2
plot(bar_3_x, bar_3_y, 'g', 'LineWidth', 2); % Bar 3

% Plot joints
plot(0, 0, 'ko', 'MarkerFaceColor', 'k'); % O joint
plot(l_0, 0, 'ko', 'MarkerFaceColor', 'k'); % O' joint
plot(bar_1_x(2), bar_1_y(2), 'ko', 'MarkerFaceColor', 'k'); % A joint
plot(bar_3_x(2), bar_3_y(2), 'ko', 'MarkerFaceColor', 'k'); % B joint

xlabel('X'); ylabel('Y');
legend('Fixed bar', 'Bar 1', 'Bar 2', 'Bar 3', 'Location', 'Best');
