import numpy as np
from equation import objectiveFunction
from scipy.optimize import minimize




def is_close_to_existing_solutions(new_solution, existing_solutions, threshold=1e-5):
    for sol in existing_solutions:
        diff = np.linalg.norm(np.array(new_solution) - np.array(sol))
        if diff < 0.8:
            return True
    return False

def optimizeFunction(parameters):
    iteration = parameters['iterations']
    threshold = parameters['threshold']
    lb = np.array(parameters['lb'])
    ub = np.array(parameters['ub'])

    # Define the range and step size for the initial guesses
    step_size_theta1 = (ub[0] - lb[0]) / iteration
    step_size_theta3 = (ub[1] - lb[1]) / iteration
    step_size_c = (ub[2] - lb[2]) / iteration

    solutions = []  # to store solutions

    for c_initial in np.arange(lb[2], ub[2] + step_size_c, step_size_c):
        for theta1_initial in np.arange(lb[0], ub[0] + step_size_theta1, step_size_theta1):
            for theta3_initial in np.arange(lb[1], ub[1] + step_size_theta3, step_size_theta3):
                initial_guess = [theta1_initial, theta3_initial, c_initial]

                result = minimize(
                    fun=objectiveFunction,
                    x0=initial_guess,
                    args=(parameters,),
                    bounds=[(lb[0], ub[0]), (lb[1], ub[1]), (lb[2], ub[2])],
                    tol=threshold
                )

                if result.success:
                    if not is_close_to_existing_solutions(result.x, solutions):
                        solutions.append(result.x)


    return solutions

