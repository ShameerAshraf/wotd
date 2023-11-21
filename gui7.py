import sys
import json
import random
import os
from PyQt5.QtWidgets import QApplication, QWidget, QVBoxLayout, QLabel
from PyQt5.QtGui import QFont

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
        file_path = os.path.join(os.path.dirname(__file__), 'output.json')  # Replace with your actual file name

        try:
            with open(file_path, 'r') as file:
                data = json.load(file)

                if isinstance(data, dict):
                    if data:
                        random_key = random.choice(list(data.keys()))
                        random_object = data[random_key]

                        # Increase the font size and add line breaks for spacing
                        font = QFont("Arial", 14)  # Adjust the size as needed
                        self.label.setFont(font)

                        text = f"<br><b>Word:</b> {random_object['mb-0 word']}<br><br><b>Definition:</b> {random_object['definition']}<br><br><b>Sentence:</b> {random_object['sentence']}<br>"
                        self.label.setText(text)
                        #self.label.setAlignment(Qt.AlignTop)  # Align text to the top

                    else:
                        self.label.setText('The JSON file is empty.')
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
