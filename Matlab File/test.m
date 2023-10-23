clear
clc

% Define transfer function
s = tf('s');
K = 1; % initial value of K
G = K/((s + 10)*(s + 1)^2);

% Bode plot for K = 1
figure;
[bodeMag, bodePhase, omega] = bode(G);
semilogx(omega, 20*log10(bodeMag(:)), 'b', 'LineWidth', 2);
hold on;

% Bode plot overlay for K = 1/242
K_new = 1/242;
G_new = K_new/((s + 10)*(s + 1)^2);
[bodeMag_new, ~, ~] = bode(G_new, omega);
semilogx(omega, 20*log10(bodeMag_new(:)), 'r--', 'LineWidth', 2);

% Formatting the plot
grid on;
title('Bode plot for Prob. 6.16(b)');
ylabel('Magnitude (dB)');
xlabel('\omega (rad/sec)');
legend('K=1', 'K=1/242');
ylim([-60, 10]);

% Phase plot
figure;
semilogx(omega, bodePhase(:), 'b', 'LineWidth', 2);

% Formatting the phase plot
grid on;
ylabel('Phase (deg)');
xlabel('\omega (rad/sec)');
title('Phase plot for Prob. 6.16(b)');
ylim([-300, 0]);
