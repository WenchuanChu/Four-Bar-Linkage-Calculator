import numpy as np


def objectiveFunction(var, parameters):
    F = equations(var, parameters)
    cost = np.sum(F ** 2)  # Square sum of the residuals to create a least-squares problem
    return cost


def equations(var, parameters):
    unknown_theta1 = var[0]
    unknown_theta3 = var[1]
    unknown_c = var[2]

    theta1_case1 = unknown_theta1 + parameters['delta_theta1_case1']
    theta1_case2 = unknown_theta1 + parameters['delta_theta1_case2']
    theta3_case1 = unknown_theta3 + parameters['delta_theta3_case1']
    theta3_case2 = unknown_theta3 + parameters['delta_theta3_case2']

    a = parameters['a']
    d = parameters['d']

    theta2, b = calculateTheta2AndB(unknown_theta1, unknown_theta3, unknown_c, a, d)
    theta2_case1, _ = calculateTheta2AndB(theta1_case1, theta3_case1, unknown_c, a, d)
    theta2_case2, _ = calculateTheta2AndB(theta1_case2, theta3_case2, unknown_c, a, d)

    # Defining the six equations
    F = np.zeros(9)
    F[0] = a * np.cos(np.radians(unknown_theta1)) + b * np.cos(np.radians(theta2)) - unknown_c * np.cos(
        np.radians(unknown_theta3)) - d
    F[1] = a * np.sin(np.radians(unknown_theta1)) + b * np.sin(np.radians(theta2)) - unknown_c * np.sin(
        np.radians(unknown_theta3))
    F[2] = a * np.cos(np.radians(theta1_case1)) + b * np.cos(np.radians(theta2_case1)) - unknown_c * np.cos(
        np.radians(theta3_case1)) - d
    F[3] = a * np.sin(np.radians(theta1_case1)) + b * np.sin(np.radians(theta2_case1)) - unknown_c * np.sin(
        np.radians(theta3_case1))
    F[4] = a * np.cos(np.radians(theta1_case2)) + b * np.cos(np.radians(theta2_case2)) - unknown_c * np.cos(
        np.radians(theta3_case2)) - d
    F[5] = a * np.sin(np.radians(theta1_case2)) + b * np.sin(np.radians(theta2_case2)) - unknown_c * np.sin(
        np.radians(theta3_case2))

    F[6] = unknown_theta1 + (180 - unknown_theta1 + theta2) + (180 - unknown_theta3) + (unknown_theta3 - theta2) - 360
    F[7] = theta1_case1 + (180 - theta1_case1 + theta2_case1) + (180 - theta3_case1) + (
                theta3_case1 - theta2_case1) - 360
    F[8] = theta1_case2 + (180 - theta1_case2 + theta2_case2) + (180 - theta3_case2) + (
                theta3_case2 - theta2_case2) - 360

    return F


def calculateTheta2AndB(theta1, theta3, c, a, d):
    c_1 = c * np.sin(np.radians(180 - theta3))
    a_1 = a * np.sin(np.radians(theta1))
    c_2 = c * np.cos(np.radians(180 - theta3))
    a_2 = a * np.cos(np.radians(theta1))
    # Calculating theta2
    theta2 = np.arctan2((c_1 - a_1), (d - c_2 - a_2))

    # Checking if sin(theta2) is close to zero
    epsilon = 1e-10
    if abs(np.sin(theta2)) < epsilon:
        b = float('inf')  # or some other value indicating error or issue
    else:
        b = (c_1 - a_1) / np.sin(theta2)

    return np.degrees(theta2), b

