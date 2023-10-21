function cost = objectiveFunction(var)
    F = equations(var);
    cost = sum(F.^2); % Square sum of the residuals to create a least-squares problem
end
