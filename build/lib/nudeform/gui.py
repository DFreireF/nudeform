import sys
import numpy as np
from PyQt5.QtWidgets import QApplication, QWidget, QLabel, QLineEdit, QPushButton, QGridLayout,QComboBox, QCheckBox
from nudeform.model import *
from nudeform.view import *

def run_plot(A, beta, gamma, granularity, save = False, dpi = 300, string = ''):
    phi, theta = np.mgrid[0:2*np.pi:granularity*1j, 0:np.pi:granularity*1j]
    Rquadr = quadrupole_shape(theta, beta=beta, gamma=gamma)
    r0 = initial_radius(A)
    R = r0 * (1 + Rquadr)
    x, y, z = xyz(R, theta, phi)

    shape_plot_3D(x, y, z, R, save = save, dpi=dpi, string = string)
    plt.show()

    plot_radius_polar_coordinates(R, phi, theta, save = save, dpi=dpi, string = string)

class App(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        grid = QGridLayout()

        # Create widgets
        self.betaInput = QLineEdit(self)
        self.gammaInput = QLineEdit(self)
        self.AInput = QLineEdit(self)
        self.granularityInput = QLineEdit(self)
        self.runButton = QPushButton('Run Plot', self)
        self.runButton.clicked.connect(self.on_click)

        # Add widgets to layout
        grid.addWidget(QLabel('Beta:'), 0, 0)
        grid.addWidget(self.betaInput, 0, 1)
        grid.addWidget(QLabel('Gamma:'), 1, 0)
        grid.addWidget(self.gammaInput, 1, 1)
        grid.addWidget(QLabel('Number of nucleons (A):'), 2, 0)
        grid.addWidget(self.AInput, 2, 1)
        grid.addWidget(QLabel('Granularity:'), 3, 0)
        grid.addWidget(self.granularityInput, 3, 1)
        grid.addWidget(self.runButton, 4, 0, 1, 2)

        self.setLayout(grid)
        self.setWindowTitle('Nuclear Deformation Plotter')
        self.setGeometry(300, 300, 400, 200)  # x, y, width, height
        self.setStyleSheet("QWidget { font-size: 14pt; } QPushButton { font-size: 16pt; min-height: 30px; }")
        
        # Add DPI selection
        self.dpiSelection = QComboBox(self)
        self.dpiSelection.addItems(["100","300","600"])
        grid.addWidget(QLabel('Select DPI:'), 5, 0)
        grid.addWidget(self.dpiSelection, 5, 1)

        # Add Save button
        self.saveCheckbox = QCheckBox('Save Plot', self)
        grid.addWidget(self.saveCheckbox, 6, 0)

        # Update Save button
        self.saveButton = QPushButton('Run and Save Plot', self)
        self.saveButton.clicked.connect(self.on_click)
        grid.addWidget(self.saveButton, 7, 0, 1, 2)
        # Add Exit button
        self.exitButton = QPushButton('Exit', self)
        self.exitButton.clicked.connect(self.close)  # Connect clicked signal to close method
        grid.addWidget(self.exitButton, 8, 0, 1, 2)  # Adjust grid position as needed

        self.show()

    def on_click(self):
        beta = float(self.betaInput.text())
        gamma = float(self.gammaInput.text())
        A = int(self.AInput.text())
        granularity = int(self.granularityInput.text())
        dpi = int(self.dpiSelection.currentText())
        save_plot = self.saveCheckbox.isChecked()
        string=f'beta={beta}_gamma={gamma}_A={A}'
        run_plot(A, beta, gamma, granularity, save=save_plot, dpi=dpi,string=string)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = App()
    sys.exit(app.exec_())
