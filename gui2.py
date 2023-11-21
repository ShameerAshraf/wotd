import sys
import json
import random
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel

class JsonViewer(QWidget):
    def __init__(self):
        super().__init__()

        self.init_ui()
        self.load_json()

    def init_ui(self):
        self.setWindowTitle('JSON Viewer')

        self.layout = QVBoxLayout()

        self.label = QLabel()
        self.layout.addWidget(self.label)

        self.setLayout(self.layout)

    def load_json(self):
        file_path = os.path.join(os.path.dirname(__file__), 'output.json')

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
