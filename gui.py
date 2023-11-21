import sys
import json
import random
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel, QPushButton, QFileDialog

class JsonViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()

    def init_ui(self):
        self.setWindowTitle('JSON Viewer')

        self.layout = QVBoxLayout()

        self.label = QLabel('Click "Load JSON" to load a JSON file.')
        self.layout.addWidget(self.label)

        load_button = QPushButton('Load JSON')
        load_button.clicked.connect(self.load_json)
        self.layout.addWidget(load_button)

        self.setLayout(self.layout)

    def load_json(self):
        options = QFileDialog.Options()
        options |= QFileDialog.ReadOnly
        file_dialog = QFileDialog()
        file_dialog.setNameFilter("JSON Files (*.json);;All Files (*)")
        file_dialog.setOptions(options)

        if file_dialog.exec_():
            file_path = file_dialog.selectedFiles()[0]
            self.display_random_object(file_path)

    def display_random_object(self, file_path):
        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                if isinstance(data, list):
                    if data:
                        random_object = random.choice(data)
                        self.label.setText(json.dumps(random_object, indent=2))
                    else:
                        self.label.setText('The JSON file is empty.')
                elif isinstance(data, dict):
                    self.label.setText('The JSON file should contain a list of objects.')
                else:
                    self.label.setText('Invalid JSON format.')

        except Exception as e:
            self.label.setText(f'Error: {str(e)}')

def main():
    app = QApplication(sys.argv)
    viewer = JsonViewer()
    viewer.show()
    sys.exit(app.exec_())

if __name__ == '__main__':
    main()
