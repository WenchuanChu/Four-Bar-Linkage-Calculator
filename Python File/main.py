import sys
from PyQt6.QtWidgets import QApplication
import gui_module
from optimizeFunction import optimizeFunction



def print_solution_as_table(sol):
    # Sort the solutions based on theta1 values
    sol.sort(key=lambda x: x[0])

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



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = gui_module.ParameterWindow(callback=optimizeFunction)
    window.show()
    app.exec()

#    parameters = window.get_parameters()
#    solution = optimizeFunction(parameters)
#    print_solution_as_table(solution)

