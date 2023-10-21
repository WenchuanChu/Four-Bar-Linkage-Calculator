import tkinter as tk
from tkinter import ttk
import json
import os

FILENAME = "parameters.json"


def get_parameters():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            default_parameters = json.load(file)
    else:
        default_parameters = {}

    def submit():
        nonlocal default_parameters
        default_parameters = {
            'iterations': int(iterations_entry.get()) if iterations_entry.get() else 0,
            'threshold': float(threshold_entry.get()) if threshold_entry.get() else 0,
            'lb': list(map(float, lb_entry.get().split(','))) if lb_entry.get() else [0],
            'ub': list(map(float, ub_entry.get().split(','))) if ub_entry.get() else [0],
            'theta1': float(theta1_entry.get()) if theta1_entry.get() else 0.0,
            'theta2': float(theta2_entry.get()) if theta2_entry.get() else 0.0,
            'theta3': float(theta3_entry.get()) if theta3_entry.get() else 0.0,
            'theta4': float(theta4_entry.get()) if theta4_entry.get() else 0.0,
            'delta_theta1_case1': float(delta_theta1_case1_entry.get()) if delta_theta1_case1_entry.get() else 0.0,
            'delta_theta2_case1': float(delta_theta2_case1_entry.get()) if delta_theta2_case1_entry.get() else 0.0,
            'delta_theta3_case1': float(delta_theta3_case1_entry.get()) if delta_theta3_case1_entry.get() else 0.0,
            'delta_theta4_case1': float(delta_theta4_case1_entry.get()) if delta_theta4_case1_entry.get() else 0.0,
            'delta_theta1_case2': float(delta_theta1_case2_entry.get()) if delta_theta1_case2_entry.get() else 0.0,
            'delta_theta2_case2': float(delta_theta2_case2_entry.get()) if delta_theta2_case2_entry.get() else 0.0,
            'delta_theta3_case2': float(delta_theta3_case2_entry.get()) if delta_theta3_case2_entry.get() else 0.0,
            'delta_theta4_case2': float(delta_theta4_case2_entry.get()) if delta_theta4_case2_entry.get() else 0.0,
            'a': float(a_entry.get()) if a_entry.get() else 0.0,
            'b': float(b_entry.get()) if b_entry.get() else 0.0,
            'c': float(c_entry.get()) if c_entry.get() else 0.0,
            'd': float(d_entry.get()) if d_entry.get() else 0.0,
        }
        with open(FILENAME, 'w') as file:
            json.dump(default_parameters, file)
        root.quit()

    root = tk.Tk()
    root.title("Input Parameters for MATLAB")

    # Create parameter input fields
    iterations_default = default_parameters.get('iterations', 0)
    iterations_entry = ttk.Entry(root)
    iterations_entry.grid(row=0, column=1)
    iterations_entry.insert(0, str(iterations_default))
    ttk.Label(root, text="Iterations:").grid(row=0, column=0)

    threshold_default = default_parameters.get('threshold', 0)
    threshold_entry = ttk.Entry(root)
    threshold_entry.grid(row=1, column=1)
    threshold_entry.insert(0, str(threshold_default))
    ttk.Label(root, text="Threshold:").grid(row=1, column=0)

    lb_default = ','.join(map(str, default_parameters.get('lb', [0.0])))
    lb_entry = ttk.Entry(root)
    lb_entry.grid(row=2, column=1)
    lb_entry.insert(0, lb_default)
    ttk.Label(root, text="lb (comma separated):").grid(row=2, column=0)

    ub_default = ','.join(map(str, default_parameters.get('ub', [0.0])))
    ub_entry = ttk.Entry(root)
    ub_entry.grid(row=3, column=1)
    ub_entry.insert(0, ub_default)
    ttk.Label(root, text="ub (comma separated):").grid(row=3, column=0)

    theta1_default = default_parameters.get('theta1', 0.0)
    theta1_entry = ttk.Entry(root)
    theta1_entry.grid(row=0, column=3)
    theta1_entry.insert(0, str(theta1_default))
    ttk.Label(root, text="Theta1:").grid(row=0, column=2)

    theta2_default = default_parameters.get('theta2', 0.0)
    theta2_entry = ttk.Entry(root)
    theta2_entry.grid(row=1, column=3)
    theta2_entry.insert(0, str(theta2_default))
    ttk.Label(root, text="Theta2:").grid(row=1, column=2)

    theta3_default = default_parameters.get('theta3', 0.0)
    theta3_entry = ttk.Entry(root)
    theta3_entry.grid(row=2, column=3)
    theta3_entry.insert(0, str(theta3_default))
    ttk.Label(root, text="Theta3:").grid(row=2, column=2)

    theta4_default = default_parameters.get('theta4', 0.0)
    theta4_entry = ttk.Entry(root)
    theta4_entry.grid(row=3, column=3)
    theta4_entry.insert(0, str(theta4_default))
    ttk.Label(root, text="Theta4:").grid(row=3, column=2)

    # ... Continue for the rest of the parameters ...

    delta_theta1_case1_default = default_parameters.get('delta_theta1_case1', 0.0)
    delta_theta1_case1_entry = ttk.Entry(root)
    delta_theta1_case1_entry.grid(row=4, column=1)
    delta_theta1_case1_entry.insert(0, str(delta_theta1_case1_default))
    ttk.Label(root, text="Delta Theta1 Case1:").grid(row=4, column=0)

    delta_theta2_case1_default = default_parameters.get('delta_theta2_case1', 0.0)
    delta_theta2_case1_entry = ttk.Entry(root)
    delta_theta2_case1_entry.grid(row=5, column=1)
    delta_theta2_case1_entry.insert(0, str(delta_theta2_case1_default))
    ttk.Label(root, text="Delta Theta2 Case1:").grid(row=5, column=0)

    delta_theta3_case1_default = default_parameters.get('delta_theta3_case1', 0.0)
    delta_theta3_case1_entry = ttk.Entry(root)
    delta_theta3_case1_entry.grid(row=6, column=1)
    delta_theta3_case1_entry.insert(0, str(delta_theta3_case1_default))
    ttk.Label(root, text="Delta Theta3 Case1:").grid(row=6, column=0)

    delta_theta4_case1_default = default_parameters.get('delta_theta4_case1', 0.0)
    delta_theta4_case1_entry = ttk.Entry(root)
    delta_theta4_case1_entry.grid(row=7, column=1)
    delta_theta4_case1_entry.insert(0, str(delta_theta4_case1_default))
    ttk.Label(root, text="Delta Theta4 Case1:").grid(row=7, column=0)

    # ... Continue for case 2 ...

    delta_theta1_case2_default = default_parameters.get('delta_theta1_case2', 0.0)
    delta_theta1_case2_entry = ttk.Entry(root)
    delta_theta1_case2_entry.grid(row=4, column=3)
    delta_theta1_case2_entry.insert(0, str(delta_theta1_case2_default))
    ttk.Label(root, text="Delta Theta1 Case2:").grid(row=4, column=2)

    delta_theta2_case2_default = default_parameters.get('delta_theta2_case2', 0.0)
    delta_theta2_case2_entry = ttk.Entry(root)
    delta_theta2_case2_entry.grid(row=5, column=3)
    delta_theta2_case2_entry.insert(0, str(delta_theta2_case2_default))
    ttk.Label(root, text="Delta Theta2 Case2:").grid(row=5, column=2)

    delta_theta3_case2_default = default_parameters.get('delta_theta3_case2', 0.0)
    delta_theta3_case2_entry = ttk.Entry(root)
    delta_theta3_case2_entry.grid(row=6, column=3)
    delta_theta3_case2_entry.insert(0, str(delta_theta3_case2_default))
    ttk.Label(root, text="Delta Theta3 Case2:").grid(row=6, column=2)

    delta_theta4_case2_default = default_parameters.get('delta_theta4_case2', 0.0)
    delta_theta4_case2_entry = ttk.Entry(root)
    delta_theta4_case2_entry.grid(row=7, column=3)
    delta_theta4_case2_entry.insert(0, str(delta_theta4_case2_default))
    ttk.Label(root, text="Delta Theta4 Case2:").grid(row=7, column=2)




    # Length entries
    a_default = default_parameters.get('a', 0.0)
    a_entry = ttk.Entry(root)
    a_entry.grid(row=8, column=1)
    a_entry.insert(0, str(a_default))
    ttk.Label(root, text="a:").grid(row=8, column=0)

    b_default = default_parameters.get('b', 0.0)
    b_entry = ttk.Entry(root)
    b_entry.grid(row=9, column=1)
    b_entry.insert(0, str(b_default))
    ttk.Label(root, text="b:").grid(row=9, column=0)

    c_default = default_parameters.get('c', 0.0)
    c_entry = ttk.Entry(root)
    c_entry.grid(row=8, column=3)
    c_entry.insert(0, str(c_default))
    ttk.Label(root, text="c:").grid(row=8, column=2)

    d_default = default_parameters.get('d', 0.0)
    d_entry = ttk.Entry(root)
    d_entry.grid(row=9, column=3)
    d_entry.insert(0, str(d_default))
    ttk.Label(root, text="d:").grid(row=9, column=2)

    submit_button = ttk.Button(root, text="Submit", command=submit)
    submit_button.grid(row=20, column=9)

    root.mainloop()
    return default_parameters


if __name__ == "__main__":
    print(get_parameters())
