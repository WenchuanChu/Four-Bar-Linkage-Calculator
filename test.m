clear
clc

% Bounds for the variables
lb = [140, 20, 0];
ub = [150, 173, 1.1];

% Placeholder for results
results = [];

% Number of iterations for optimization
num_iterations = 40000;

% Threshold for objective function value
threshold = 10e-10;

options = optimoptions('fmincon','Display','off','Algorithm','sqp');

for i = 1:num_iterations
    % Random initial guess within bounds
    x0 = [rand()*180, rand()*180, rand()];

    % Using fmincon to minimize
% µ÷ÓÃfmincon
    [x, fval] = fmincon(@func_to_minimize, x0, [], [], [], [], lb, ub, [], options);
    if mod(i, 100) == 0
        disp(i);
    end
    % If the objective function value is less than the threshold and theta2 is less than 90, store the result
    if fval < threshold 
        results = [results; x];
    end
end

% Sort results by column 'b' in descending order
results = sortrows(results, 1);

% Adding variable names at the top
headers = {'theta1', 'theta3', 'c'};
results = [headers; num2cell(results)];
disp(results);



