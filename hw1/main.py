from PyQt5.QtWidgets import *
import sys


app = QApplication([])
window = QWidget()
layout = QVBoxLayout()

#prob1
prob1_group=QGroupBox("1.Camera Calibration", window)
layout.addWidget(prob1_group)
prob1_layout=QVBoxLayout()
prob1_group.setLayout(prob1_layout)

prob1_layout.addWidget(QPushButton('Corner detection'))
prob1_layout.addWidget(QPushButton('Find the intrinsic matrix'))
prob1_layout.addWidget(QPushButton('Find the extrinsic matrix'))
prob1_layout.addWidget(QPushButton('Find the distortion matrix'))
prob1_layout.addWidget(QPushButton('Show the undistorted result'))

#prob2

window.setLayout(layout)
window.show()
app.exec()
