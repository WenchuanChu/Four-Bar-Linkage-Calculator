function solutions = optimizeFunction(parameterData)
    parameter = parameterData();
    iteration = parameter.iterations;
    threshold = parameter.threshold;
    lb = parameter.lb;
    ub = parameter.ub;
    
    % Define the range and step size for the initial guesses
    theta1_range = [lb(1), ub(1)];
    theta3_range = [lb(2), ub(2)]; 
    c_range = [lb(3), ub(3)]; 
    
    step_size_theta1 = (ub(1) - lb(1)) / iteration;
    step_size_theta3 = (ub(2) - lb(2)) / iteration;
    step_size_c = (ub(3) - lb(3)) / iteration;

    options = optimoptions('fmincon', 'Display', 'none', 'Algorithm', 'interior-point', 'OptimalityTolerance', threshold);
    
    solutions = []; % to store solutions
    for c_initial = c_range(1):step_size_c:c_range(2)
        for theta1_initial = theta1_range(1):step_size_theta1:theta1_range(2)
            for theta3_initial = theta3_range(1):step_size_theta3:theta3_range(2)
                initial_guess = [theta1_initial, theta3_initial, c_initial];
                
                % Use fmincon to minimize the objective function
                solution = fmincon(@objectiveFunction, initial_guess, [], [], [], [], lb, ub, [], options);
                
                % Check if the solution is within bounds (optional)
                if all(solution >= lb) && all(solution <= ub)
                   solutions = [solutions; solution];
                end
            end
        end
    end
    
    % Remove duplicate solutions (based on a tolerance)
    tolerance = 0.1; % adjust as necessary
    solutions = uniquetol(solutions, tolerance, 'ByRows', true);
    

end




