import sys
import json
import os
from PyQt6.QtWidgets import (QApplication, QWidget, QGridLayout, QLabel, QLineEdit,
                             QPushButton, QTableWidget, QTableWidgetItem)
from PyQt6.QtCore import Qt

FILENAME = "parameters.json"


def float_list_to_str(lst):
    return ', '.join(map(str, lst))
class ParameterWindow(QWidget):
    def __init__(self, callback=None):
        super().__init__()
        self.callback = callback
        self.init_ui()

    def init_ui(self):
        layout = QGridLayout()

        self.solution_table = QTableWidget(self)
        self.solution_table.setColumnCount(3)  # 根据你的数据有3列
        self.solution_table.setHorizontalHeaderLabels(['Theta1', 'Theta2', 'Length_c'])  # 你可以替换为更合适的列名
        layout.addWidget(self.solution_table, 10, 0, 1, 4)  # 这将把表格放在适当的位置，你可以根据需要调整它

        # Load defaults
        if os.path.exists(FILENAME):
            with open(FILENAME, 'r') as file:
                self.default_parameters = json.load(file)
        else:
            self.default_parameters = {}

        # Create widgets and add them to the layout
        self.iterations_entry = self.create_line_edit(layout,"Iterations:", 0, 0, 'iterations')
        self.threshold_entry = self.create_line_edit(layout,"Threshold:", 1, 0, 'threshold')
        self.lb_entry = self.create_line_edit(layout, "lb (comma separated):", 2, 0, 'lb', float_list_to_str)
        self.ub_entry = self.create_line_edit(layout, "ub (comma separated):", 3, 0, 'ub', float_list_to_str)

        self.theta1_entry = self.create_line_edit(layout,"Theta1:", 0, 2, 'theta1')
        self.theta2_entry = self.create_line_edit(layout,"Theta2:", 1, 2, 'theta2')
        self.theta3_entry = self.create_line_edit(layout,"Theta3:", 2, 2, 'theta3')
        self.theta4_entry = self.create_line_edit(layout,"Theta4:", 3, 2, 'theta4')

        # Continue for the rest of the parameters
        self.delta_theta1_case1_entry = self.create_line_edit(layout,"Delta Theta1 Case1:", 4, 0, 'delta_theta1_case1')
        self.delta_theta2_case1_entry = self.create_line_edit(layout,"Delta Theta2 Case1:", 5, 0, 'delta_theta2_case1')
        self.delta_theta3_case1_entry = self.create_line_edit(layout,"Delta Theta3 Case1:", 6, 0, 'delta_theta3_case1')
        self.delta_theta4_case1_entry = self.create_line_edit(layout,"Delta Theta4 Case1:", 7, 0, 'delta_theta4_case1')

        self.delta_theta1_case2_entry = self.create_line_edit(layout,"Delta Theta1 Case2:", 4, 2, 'delta_theta1_case2')
        self.delta_theta2_case2_entry = self.create_line_edit(layout,"Delta Theta2 Case2:", 5, 2, 'delta_theta2_case2')
        self.delta_theta3_case2_entry = self.create_line_edit(layout,"Delta Theta3 Case2:", 6, 2, 'delta_theta3_case2')
        self.delta_theta4_case2_entry = self.create_line_edit(layout,"Delta Theta4 Case2:", 7, 2, 'delta_theta4_case2')
        self.a_entry = self.create_line_edit(layout,"a:", 8, 0, 'a')
        self.b_entry = self.create_line_edit(layout,"b:", 9, 0, 'b')
        self.c_entry = self.create_line_edit(layout,"c:", 8, 2, 'c')
        self.d_entry = self.create_line_edit(layout,"d:", 9, 2, 'd')

        submit_button = QPushButton("Submit", self)
        submit_button.clicked.connect(self.submit)
        layout.addWidget(submit_button, 20, 9)

        self.setLayout(layout)

    def create_line_edit(self, layout, label_text, row, col, key, formatter=str):
        label = QLabel(label_text)
        entry = QLineEdit()
        label.setAlignment(Qt.AlignmentFlag.AlignRight | Qt.AlignmentFlag.AlignVCenter)

        layout.addWidget(label, row, col)
        layout.addWidget(entry, row, col + 1)
        entry.setText(formatter(self.default_parameters.get(key, '')))
        return entry

    def update_table(self, data):
        self.solution_table.setRowCount(len(data))
        for row, row_data in enumerate(data):
            for col, item in enumerate(row_data):
                self.solution_table.setItem(row, col, QTableWidgetItem(str(item)))
    def submit(self):

        # Extract values, update default_parameters, and write to JSON file
        # For simplicity, the extraction method assumes all values are float.
        # Adjust as necessary if other types are needed.
        self.default_parameters.update({
            'iterations': float(self.iterations_entry.text()),
            'threshold': float(self.threshold_entry.text()),
            'lb': list(map(float, self.lb_entry.text().split(','))),
            'ub': list(map(float, self.ub_entry.text().split(','))),
            'theta1': float(self.theta1_entry.text()),
            'theta2': float(self.theta2_entry.text()),
            'theta3': float(self.theta3_entry.text()),
            'theta4': float(self.theta4_entry.text()),
            'delta_theta1_case1': float(self.delta_theta1_case1_entry.text()),
            'delta_theta2_case1': float(self.delta_theta2_case1_entry.text()),
            'delta_theta3_case1': float(self.delta_theta3_case1_entry.text()),
            'delta_theta4_case1': float(self.delta_theta4_case1_entry.text()),
            'delta_theta1_case2': float(self.delta_theta1_case2_entry.text()),
            'delta_theta2_case2': float(self.delta_theta2_case2_entry.text()),
            'delta_theta3_case2': float(self.delta_theta3_case2_entry.text()),
            'delta_theta4_case2': float(self.delta_theta4_case2_entry.text()),
            'a': float(self.a_entry.text()),
            'b': float(self.b_entry.text()),
            'c': float(self.c_entry.text()),
            'd': float(self.d_entry.text()),
        })

        with open(FILENAME, 'w') as file:
            json.dump(self.default_parameters, file)

        if self.callback:
            print('Start Computing')
            solutions = self.callback(self.default_parameters)
            # 对solutions按照column1进行从小到大排序
            sorted_solutions = sorted(solutions, key=lambda x: x[0])
            # 保留两位小数并更新表格
            formatted_solutions = [[round(value, 2) for value in row] for row in sorted_solutions]
            self.update_table(formatted_solutions)

    def get_parameters(self):
        return self.default_parameters



if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = ParameterWindow()
    window.show()
    sys.exit(app.exec())

