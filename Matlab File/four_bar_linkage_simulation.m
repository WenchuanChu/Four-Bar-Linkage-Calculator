%% Four-bar linkage
% Animation of a four-bar linkage.
%
% Reference: 
%
% Tang, C.P., 2010. Lagrangian dynamic formulation of a four-bar mechanism
% with minimal coordinates.
%
%% 
clear ; close all ; clc
%% Parameters
% Bars
l_1 = 1.0;                      % Length bar a                  [m]
l_2 = 0.3;                     % Length bar b                  [m]
l_3 = 0.5;                      % Length bar c                  [m]
l_0 = 0.3;                        % Length bar d                  [m]
% Video
tF      = 10;                   % Final time                    [s]
fR      = 60;                   % Frame rate                    [fps]
dt      = 1/fR;                 % Time resolution               [s]
time    = linspace(0,tF,tF*fR); % Time                          [s]
% Bar a rotation
w = 2;                          % Angular velocity              [rad/s]
th_vet = w*time';
% Definitions
k_1 = -2*l_1*l_3*sin(th_vet);
k_2 = 2*l_3*(l_0-l_1*cos(th_vet));
k_3 = l_0^2 + l_1^2 - l_2^2 + l_3^2 - 2*l_0*l_1*cos(th_vet);
% phi
phi_vet = 2*atan2(-k_1-sqrt(k_1.^2+k_2.^2-k_3.^2),k_3-k_2);
% alpha
alpha_vet = atan2(-l_1*sin(th_vet)+l_3*sin(phi_vet),l_0-l_1*cos(th_vet)+l_3*cos(phi_vet));
point_A_x_cum = l_1*cos(th_vet); % Point A cummulative
point_A_y_cum = l_1*sin(th_vet); % Point A cummulative
point_B_x_cum = l_0+l_3*cos(phi_vet); % Point B cummulative
point_B_y_cum = l_3*sin(phi_vet); % Point B cummulative
%% Animation
color = cool(5); % Colormap
figure
% set(gcf,'Position',[50 50 1280 720])  % YouTube: 720p
% set(gcf,'Position',[50 50 854 480])   % YouTube: 480p
set(gcf,'Position',[50 50 640 640])     % Social
hold on ; grid on ; box on ; axis equal
set(gca,'FontName','Verdana','FontSize',18)
title('Four-bar linkage')
% Create and open video writer object
v = VideoWriter('four_bar_linkage.mp4','MPEG-4');
v.Quality   = 100;
v.FrameRate = fR;
open(v);
for i=1:length(time)
    cla
    % Angles
    th      = th_vet(i);
    phi     = phi_vet(i);
    alpha   = alpha_vet(i);
    % Bar 1
    bar_1_x = [0 l_1*cos(th)];
    bar_1_y = [0 l_1*sin(th)];
    
    % Bar 2
    bar_2_x = [l_1*cos(th) l_1*cos(th)+l_2*cos(alpha)];
    bar_2_y = [l_1*sin(th) l_1*sin(th)+l_2*sin(alpha)];
    % Bar 3
    bar_3_x = [l_0 l_0+l_3*cos(phi)];
    bar_3_y = [0 l_3*sin(phi)];
    
    % Trajectory
    % Point A
    plot(point_A_x_cum(1:i),point_A_y_cum(1:i),'Color',color(1,:),'LineWidth',3) % Point A trajectory
    % Point B
    plot(point_B_x_cum(1:i),point_B_y_cum(1:i),'Color',color(5,:),'LineWidth',3) % Point B trajectory
    
    % Fixed bar
    plot([bar_1_x(1) bar_3_x(1)],[0 0],'k','LineWidth',7)           % Bar 0
    
    % Bars attached to fixed bar
    plot(bar_1_x,bar_1_y,'Color',color(2,:),'LineWidth',7)          % Bar 1
    plot(bar_3_x,bar_3_y,'Color',color(4,:),'LineWidth',7)          % Bar 3
    
    % Bearings
    plot(bar_1_x(1),bar_1_y(1),'k^','MarkerFaceColor','k','MarkerSize',15) % Point O
    plot(bar_3_x(1),bar_3_y(1),'k^','MarkerFaceColor','k','MarkerSize',15) % Point O'
    
    % Bar 2
    plot(bar_2_x,bar_2_y,'Color',color(3,:),'LineWidth',7) % Bar 2
    
    % Points 
    plot(bar_2_x(1),bar_2_y(1),'ko','MarkerFaceColor',color(1,:),'MarkerSize',10)      % Point A
    plot(bar_3_x(end),bar_3_y(end),'ko','MarkerFaceColor',color(5,:),'MarkerSize',10)  % Point B
    
    %Setting axes limits
    x_range = [point_A_x_cum ;  point_B_x_cum];
    y_range = [point_A_y_cum ;  point_B_y_cum];
    
    set(gca,'xlim',[min(x_range)-0.2*(max(x_range)-min(x_range))
                    max(x_range)+0.2*(max(x_range)-min(x_range))]...
           ,'ylim',[min(y_range)-0.2*(max(y_range)-min(y_range))
                    max(y_range)+0.2*(max(y_range)-min(y_range))])
    set(gca,'xtick',[],'ytick',[])
    
    frame = getframe(gcf);
    writeVideo(v,frame);
    
end
close(v);