import matlab.engine
import gui_module  # 请确保这个模块的名称是正确的


def python_dict_to_matlab_struct(py_dict):
    return {key: matlab.double([val]) if isinstance(val, (int, float)) else matlab.double(val) for key, val in py_dict.items()}


def print_solution_as_table(sol):
    # Define the widths for each column
    width_theta1 = 10
    width_theta3 = 10
    width_c = 10

    # Print the header with appropriate spacing
    print(
        "{:<{width1}}{:<{width2}}{:<{width3}}".format("theta1", "theta3", "c", width1=width_theta1, width2=width_theta3,
                                                      width3=width_c))
    print("-" * (width_theta1 + width_theta3 + width_c))

    # Print each row of the solution with formatting
    for row in sol:
        print("{:<{width1}.2f}{:<{width2}.2f}{:<{width3}.2f}".format(row[0], row[1], row[2], width1=width_theta1,
                                                                     width2=width_theta3, width3=width_c))



parameters = gui_module.get_parameters()
print('Start Computing')
matlab_struct_parameters = python_dict_to_matlab_struct(parameters)


eng = matlab.engine.start_matlab()
solution = eng.optimizeFunction(matlab_struct_parameters)
print_solution_as_table(solution)
eng.quit()
