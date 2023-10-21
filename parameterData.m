function [parameter] = parameterData()
    parameter.iterations = 10;
    parameter.threshold = 1e-24;
    parameter.lb = [0, 0, 0];
    parameter.ub = [180, 180, 2];
end