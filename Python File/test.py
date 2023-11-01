
self.table = QTableWidget(self)
self.table.setColumnCount(2)
self.table.setHorizontalHeaderLabels(["Parameter", "Value"])
layout.addWidget(self.table, 10, 0, 10, 4)  # 这将占据很大的空间，你可以根据需要调整
self.update_table()

self.update_table()


def update_table(self):
    self.table.setRowCount(len(self.get_parameters))
    for row, (key, value) in enumerate(self.default_parameters.items()):
        self.table.setItem(row, 0, QTableWidgetItem(key))
        if isinstance(value, list):
            self.table.setItem(row, 1, QTableWidgetItem(float_list_to_str(value)))
        else:
            self.table.setItem(row, 1, QTableWidgetItem(str(value)))