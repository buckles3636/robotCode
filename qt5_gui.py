# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'robocats_gui_qt5_ui.ui'
#
# Created by: PyQt5 UI code generator 5.15.4
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(1436, 1055)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.console = QtWidgets.QTextBrowser(self.centralwidget)
        self.console.setGeometry(QtCore.QRect(360, 760, 681, 192))
        self.console.setMinimumSize(QtCore.QSize(681, 192))
        self.console.setObjectName("console")
        self.e_stop_button = QtWidgets.QPushButton(self.centralwidget)
        self.e_stop_button.setGeometry(QtCore.QRect(1150, 760, 192, 192))
        self.e_stop_button.setMinimumSize(QtCore.QSize(192, 192))
        self.e_stop_button.setAutoFillBackground(False)
        self.e_stop_button.setObjectName("e_stop_button")
        self.control_buttons = QtWidgets.QWidget(self.centralwidget)
        self.control_buttons.setGeometry(QtCore.QRect(40, 740, 281, 241))
        self.control_buttons.setMinimumSize(QtCore.QSize(220, 220))
        self.control_buttons.setObjectName("control_buttons")
        self.widget = QtWidgets.QWidget(self.control_buttons)
        self.widget.setGeometry(QtCore.QRect(40, 10, 201, 209))
        self.widget.setObjectName("widget")
        self.verticalLayout_8 = QtWidgets.QVBoxLayout(self.widget)
        self.verticalLayout_8.setContentsMargins(0, 0, 0, 0)
        self.verticalLayout_8.setObjectName("verticalLayout_8")
        self.neutral_button = QtWidgets.QPushButton(self.widget)
        self.neutral_button.setObjectName("neutral_button")
        self.verticalLayout_8.addWidget(self.neutral_button)
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout()
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.verticalLayout_7 = QtWidgets.QVBoxLayout()
        self.verticalLayout_7.setObjectName("verticalLayout_7")
        self.dive_button = QtWidgets.QPushButton(self.widget)
        self.dive_button.setObjectName("dive_button")
        self.verticalLayout_7.addWidget(self.dive_button)
        self.surface_button = QtWidgets.QPushButton(self.widget)
        self.surface_button.setObjectName("surface_button")
        self.verticalLayout_7.addWidget(self.surface_button)
        self.all_motors_button = QtWidgets.QPushButton(self.widget)
        self.all_motors_button.setObjectName("all_motors_button")
        self.verticalLayout_7.addWidget(self.all_motors_button)
        self.seq_test_button = QtWidgets.QPushButton(self.widget)
        self.seq_test_button.setObjectName("seq_test_button")
        self.verticalLayout_7.addWidget(self.seq_test_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_7)
        self.verticalLayout_6 = QtWidgets.QVBoxLayout()
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.forward_button = QtWidgets.QPushButton(self.widget)
        self.forward_button.setObjectName("forward_button")
        self.verticalLayout_6.addWidget(self.forward_button)
        self.hover_forward_button = QtWidgets.QPushButton(self.widget)
        self.hover_forward_button.setObjectName("hover_forward_button")
        self.verticalLayout_6.addWidget(self.hover_forward_button)
        self.reverse_button = QtWidgets.QPushButton(self.widget)
        self.reverse_button.setObjectName("reverse_button")
        self.verticalLayout_6.addWidget(self.reverse_button)
        self.hover_spin_button = QtWidgets.QPushButton(self.widget)
        self.hover_spin_button.setObjectName("hover_spin_button")
        self.verticalLayout_6.addWidget(self.hover_spin_button)
        self.horizontalLayout_2.addLayout(self.verticalLayout_6)
        self.verticalLayout_8.addLayout(self.horizontalLayout_2)
        self.widget1 = QtWidgets.QWidget(self.centralwidget)
        self.widget1.setGeometry(QtCore.QRect(430, 420, 500, 82))
        self.widget1.setObjectName("widget1")
        self.depth_pressure_data_h_layout = QtWidgets.QHBoxLayout(self.widget1)
        self.depth_pressure_data_h_layout.setContentsMargins(0, 0, 0, 0)
        self.depth_pressure_data_h_layout.setObjectName("depth_pressure_data_h_layout")
        self.depth_widget = QtWidgets.QWidget(self.widget1)
        self.depth_widget.setMinimumSize(QtCore.QSize(120, 80))
        self.depth_widget.setObjectName("depth_widget")
        self.depth_lcd = QtWidgets.QLCDNumber(self.depth_widget)
        self.depth_lcd.setGeometry(QtCore.QRect(3, 22, 111, 51))
        self.depth_lcd.setMinimumSize(QtCore.QSize(111, 51))
        self.depth_lcd.setObjectName("depth_lcd")
        self.label_16 = QtWidgets.QLabel(self.depth_widget)
        self.label_16.setGeometry(QtCore.QRect(8, 0, 101, 20))
        self.label_16.setMinimumSize(QtCore.QSize(101, 20))
        self.label_16.setObjectName("label_16")
        self.depth_pressure_data_h_layout.addWidget(self.depth_widget)
        self.altitude_widget = QtWidgets.QWidget(self.widget1)
        self.altitude_widget.setMinimumSize(QtCore.QSize(120, 80))
        self.altitude_widget.setObjectName("altitude_widget")
        self.altitude_lcd = QtWidgets.QLCDNumber(self.altitude_widget)
        self.altitude_lcd.setGeometry(QtCore.QRect(3, 22, 111, 51))
        self.altitude_lcd.setMinimumSize(QtCore.QSize(111, 51))
        self.altitude_lcd.setObjectName("altitude_lcd")
        self.label_5 = QtWidgets.QLabel(self.altitude_widget)
        self.label_5.setGeometry(QtCore.QRect(8, 0, 101, 20))
        self.label_5.setMinimumSize(QtCore.QSize(101, 20))
        self.label_5.setObjectName("label_5")
        self.depth_pressure_data_h_layout.addWidget(self.altitude_widget)
        self.temperature_widget = QtWidgets.QWidget(self.widget1)
        self.temperature_widget.setMinimumSize(QtCore.QSize(120, 80))
        self.temperature_widget.setObjectName("temperature_widget")
        self.temperature_lcd = QtWidgets.QLCDNumber(self.temperature_widget)
        self.temperature_lcd.setGeometry(QtCore.QRect(3, 22, 111, 51))
        self.temperature_lcd.setMinimumSize(QtCore.QSize(111, 51))
        self.temperature_lcd.setObjectName("temperature_lcd")
        self.label_7 = QtWidgets.QLabel(self.temperature_widget)
        self.label_7.setGeometry(QtCore.QRect(8, 0, 101, 20))
        self.label_7.setMinimumSize(QtCore.QSize(101, 20))
        self.label_7.setObjectName("label_7")
        self.depth_pressure_data_h_layout.addWidget(self.temperature_widget)
        self.pressure_widget = QtWidgets.QWidget(self.widget1)
        self.pressure_widget.setMinimumSize(QtCore.QSize(120, 80))
        self.pressure_widget.setObjectName("pressure_widget")
        self.pressure_lcd = QtWidgets.QLCDNumber(self.pressure_widget)
        self.pressure_lcd.setGeometry(QtCore.QRect(3, 22, 111, 51))
        self.pressure_lcd.setMinimumSize(QtCore.QSize(111, 51))
        self.pressure_lcd.setObjectName("pressure_lcd")
        self.label_6 = QtWidgets.QLabel(self.pressure_widget)
        self.label_6.setGeometry(QtCore.QRect(8, 0, 101, 20))
        self.label_6.setMinimumSize(QtCore.QSize(101, 20))
        self.label_6.setObjectName("label_6")
        self.depth_pressure_data_h_layout.addWidget(self.pressure_widget)
        self.widget2 = QtWidgets.QWidget(self.centralwidget)
        self.widget2.setGeometry(QtCore.QRect(500, 320, 374, 82))
        self.widget2.setObjectName("widget2")
        self.imu_data_h_layout = QtWidgets.QHBoxLayout(self.widget2)
        self.imu_data_h_layout.setContentsMargins(0, 0, 0, 0)
        self.imu_data_h_layout.setObjectName("imu_data_h_layout")
        self.pitch_widget = QtWidgets.QWidget(self.widget2)
        self.pitch_widget.setMinimumSize(QtCore.QSize(120, 80))
        self.pitch_widget.setObjectName("pitch_widget")
        self.pitch_lcd = QtWidgets.QLCDNumber(self.pitch_widget)
        self.pitch_lcd.setGeometry(QtCore.QRect(3, 22, 111, 51))
        self.pitch_lcd.setMinimumSize(QtCore.QSize(111, 51))
        self.pitch_lcd.setObjectName("pitch_lcd")
        self.label = QtWidgets.QLabel(self.pitch_widget)
        self.label.setGeometry(QtCore.QRect(8, 0, 101, 20))
        self.label.setMinimumSize(QtCore.QSize(101, 20))
        self.label.setObjectName("label")
        self.imu_data_h_layout.addWidget(self.pitch_widget)
        self.yaw_widget = QtWidgets.QWidget(self.widget2)
        self.yaw_widget.setMinimumSize(QtCore.QSize(120, 80))
        self.yaw_widget.setObjectName("yaw_widget")
        self.yaw_lcd = QtWidgets.QLCDNumber(self.yaw_widget)
        self.yaw_lcd.setGeometry(QtCore.QRect(3, 22, 111, 51))
        self.yaw_lcd.setMinimumSize(QtCore.QSize(111, 51))
        self.yaw_lcd.setObjectName("yaw_lcd")
        self.label_3 = QtWidgets.QLabel(self.yaw_widget)
        self.label_3.setGeometry(QtCore.QRect(8, 0, 101, 20))
        self.label_3.setMinimumSize(QtCore.QSize(101, 20))
        self.label_3.setObjectName("label_3")
        self.imu_data_h_layout.addWidget(self.yaw_widget)
        self.roll_widget = QtWidgets.QWidget(self.widget2)
        self.roll_widget.setMinimumSize(QtCore.QSize(120, 80))
        self.roll_widget.setObjectName("roll_widget")
        self.roll_lcd = QtWidgets.QLCDNumber(self.roll_widget)
        self.roll_lcd.setGeometry(QtCore.QRect(3, 22, 111, 51))
        self.roll_lcd.setMinimumSize(QtCore.QSize(111, 51))
        self.roll_lcd.setObjectName("roll_lcd")
        self.label_4 = QtWidgets.QLabel(self.roll_widget)
        self.label_4.setGeometry(QtCore.QRect(8, 0, 101, 20))
        self.label_4.setMinimumSize(QtCore.QSize(101, 20))
        self.label_4.setObjectName("label_4")
        self.imu_data_h_layout.addWidget(self.roll_widget)
        self.widget3 = QtWidgets.QWidget(self.centralwidget)
        self.widget3.setGeometry(QtCore.QRect(300, 120, 725, 159))
        self.widget3.setObjectName("widget3")
        self.motor_h_layout = QtWidgets.QHBoxLayout(self.widget3)
        self.motor_h_layout.setContentsMargins(0, 0, 0, 0)
        self.motor_h_layout.setObjectName("motor_h_layout")
        self.motor_1_lh = QtWidgets.QWidget(self.widget3)
        self.motor_1_lh.setObjectName("motor_1_lh")
        self.gridLayout = QtWidgets.QGridLayout(self.motor_1_lh)
        self.gridLayout.setObjectName("gridLayout")
        self.label_8 = QtWidgets.QLabel(self.motor_1_lh)
        self.label_8.setObjectName("label_8")
        self.gridLayout.addWidget(self.label_8, 0, 0, 1, 1)
        self.motor_1_spin = QtWidgets.QSpinBox(self.motor_1_lh)
        self.motor_1_spin.setMinimum(-100)
        self.motor_1_spin.setMaximum(100)
        self.motor_1_spin.setObjectName("motor_1_spin")
        self.gridLayout.addWidget(self.motor_1_spin, 1, 0, 1, 1)
        self.motor_1_slider = QtWidgets.QSlider(self.motor_1_lh)
        self.motor_1_slider.setMinimum(-100)
        self.motor_1_slider.setMaximum(100)
        self.motor_1_slider.setProperty("value", 0)
        self.motor_1_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_1_slider.setObjectName("motor_1_slider")
        self.gridLayout.addWidget(self.motor_1_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_1_lh)
        self.motor_2_rh = QtWidgets.QWidget(self.widget3)
        self.motor_2_rh.setObjectName("motor_2_rh")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.motor_2_rh)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_9 = QtWidgets.QLabel(self.motor_2_rh)
        self.label_9.setObjectName("label_9")
        self.gridLayout_2.addWidget(self.label_9, 0, 0, 1, 1)
        self.motor_2_spin = QtWidgets.QSpinBox(self.motor_2_rh)
        self.motor_2_spin.setMinimum(-100)
        self.motor_2_spin.setMaximum(100)
        self.motor_2_spin.setObjectName("motor_2_spin")
        self.gridLayout_2.addWidget(self.motor_2_spin, 1, 0, 1, 1)
        self.motor_2_slider = QtWidgets.QSlider(self.motor_2_rh)
        self.motor_2_slider.setMinimum(-100)
        self.motor_2_slider.setMaximum(100)
        self.motor_2_slider.setProperty("value", 0)
        self.motor_2_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_2_slider.setObjectName("motor_2_slider")
        self.gridLayout_2.addWidget(self.motor_2_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_2_rh)
        self.motor_3_fh = QtWidgets.QWidget(self.widget3)
        self.motor_3_fh.setObjectName("motor_3_fh")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.motor_3_fh)
        self.gridLayout_8.setObjectName("gridLayout_8")
        self.label_15 = QtWidgets.QLabel(self.motor_3_fh)
        self.label_15.setObjectName("label_15")
        self.gridLayout_8.addWidget(self.label_15, 0, 0, 1, 1)
        self.motor_3_spin = QtWidgets.QSpinBox(self.motor_3_fh)
        self.motor_3_spin.setMinimum(-100)
        self.motor_3_spin.setMaximum(100)
        self.motor_3_spin.setObjectName("motor_3_spin")
        self.gridLayout_8.addWidget(self.motor_3_spin, 1, 0, 1, 1)
        self.motor_3_slider = QtWidgets.QSlider(self.motor_3_fh)
        self.motor_3_slider.setMinimum(-100)
        self.motor_3_slider.setMaximum(100)
        self.motor_3_slider.setProperty("value", 0)
        self.motor_3_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_3_slider.setObjectName("motor_3_slider")
        self.gridLayout_8.addWidget(self.motor_3_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_3_fh)
        self.motor_4_bh = QtWidgets.QWidget(self.widget3)
        self.motor_4_bh.setObjectName("motor_4_bh")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.motor_4_bh)
        self.gridLayout_6.setObjectName("gridLayout_6")
        self.label_13 = QtWidgets.QLabel(self.motor_4_bh)
        self.label_13.setObjectName("label_13")
        self.gridLayout_6.addWidget(self.label_13, 0, 0, 1, 1)
        self.motor_4_spin = QtWidgets.QSpinBox(self.motor_4_bh)
        self.motor_4_spin.setMinimum(-100)
        self.motor_4_spin.setMaximum(100)
        self.motor_4_spin.setObjectName("motor_4_spin")
        self.gridLayout_6.addWidget(self.motor_4_spin, 1, 0, 1, 1)
        self.motor_4_slider = QtWidgets.QSlider(self.motor_4_bh)
        self.motor_4_slider.setMinimum(-100)
        self.motor_4_slider.setMaximum(100)
        self.motor_4_slider.setProperty("value", 0)
        self.motor_4_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_4_slider.setObjectName("motor_4_slider")
        self.gridLayout_6.addWidget(self.motor_4_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_4_bh)
        self.motor_5_fvh = QtWidgets.QWidget(self.widget3)
        self.motor_5_fvh.setObjectName("motor_5_fvh")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.motor_5_fvh)
        self.gridLayout_7.setObjectName("gridLayout_7")
        self.label_14 = QtWidgets.QLabel(self.motor_5_fvh)
        self.label_14.setObjectName("label_14")
        self.gridLayout_7.addWidget(self.label_14, 0, 0, 1, 1)
        self.motor_5_spin = QtWidgets.QSpinBox(self.motor_5_fvh)
        self.motor_5_spin.setMinimum(-100)
        self.motor_5_spin.setMaximum(100)
        self.motor_5_spin.setObjectName("motor_5_spin")
        self.gridLayout_7.addWidget(self.motor_5_spin, 1, 0, 1, 1)
        self.motor_5_slider = QtWidgets.QSlider(self.motor_5_fvh)
        self.motor_5_slider.setMinimum(-100)
        self.motor_5_slider.setMaximum(100)
        self.motor_5_slider.setProperty("value", 0)
        self.motor_5_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_5_slider.setObjectName("motor_5_slider")
        self.gridLayout_7.addWidget(self.motor_5_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_5_fvh)
        self.motor_6_frv = QtWidgets.QWidget(self.widget3)
        self.motor_6_frv.setObjectName("motor_6_frv")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.motor_6_frv)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.label_11 = QtWidgets.QLabel(self.motor_6_frv)
        self.label_11.setObjectName("label_11")
        self.gridLayout_4.addWidget(self.label_11, 0, 0, 1, 1)
        self.motor_6_spin = QtWidgets.QSpinBox(self.motor_6_frv)
        self.motor_6_spin.setMinimum(-100)
        self.motor_6_spin.setMaximum(100)
        self.motor_6_spin.setObjectName("motor_6_spin")
        self.gridLayout_4.addWidget(self.motor_6_spin, 1, 0, 1, 1)
        self.motor_6_slider = QtWidgets.QSlider(self.motor_6_frv)
        self.motor_6_slider.setMinimum(-100)
        self.motor_6_slider.setMaximum(100)
        self.motor_6_slider.setProperty("value", 0)
        self.motor_6_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_6_slider.setObjectName("motor_6_slider")
        self.gridLayout_4.addWidget(self.motor_6_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_6_frv)
        self.motor_7_blv = QtWidgets.QWidget(self.widget3)
        self.motor_7_blv.setObjectName("motor_7_blv")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.motor_7_blv)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.label_12 = QtWidgets.QLabel(self.motor_7_blv)
        self.label_12.setObjectName("label_12")
        self.gridLayout_5.addWidget(self.label_12, 0, 0, 1, 1)
        self.motor_7_spin = QtWidgets.QSpinBox(self.motor_7_blv)
        self.motor_7_spin.setMinimum(-100)
        self.motor_7_spin.setMaximum(100)
        self.motor_7_spin.setObjectName("motor_7_spin")
        self.gridLayout_5.addWidget(self.motor_7_spin, 1, 0, 1, 1)
        self.motor_7_slider = QtWidgets.QSlider(self.motor_7_blv)
        self.motor_7_slider.setMinimum(-100)
        self.motor_7_slider.setMaximum(100)
        self.motor_7_slider.setProperty("value", 0)
        self.motor_7_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_7_slider.setObjectName("motor_7_slider")
        self.gridLayout_5.addWidget(self.motor_7_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_7_blv)
        self.motor_8_brv = QtWidgets.QWidget(self.widget3)
        self.motor_8_brv.setObjectName("motor_8_brv")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.motor_8_brv)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.label_10 = QtWidgets.QLabel(self.motor_8_brv)
        self.label_10.setObjectName("label_10")
        self.gridLayout_3.addWidget(self.label_10, 0, 0, 1, 1)
        self.motor_8_spin = QtWidgets.QSpinBox(self.motor_8_brv)
        self.motor_8_spin.setMinimum(-100)
        self.motor_8_spin.setMaximum(100)
        self.motor_8_spin.setObjectName("motor_8_spin")
        self.gridLayout_3.addWidget(self.motor_8_spin, 1, 0, 1, 1)
        self.motor_8_slider = QtWidgets.QSlider(self.motor_8_brv)
        self.motor_8_slider.setMinimum(-100)
        self.motor_8_slider.setMaximum(100)
        self.motor_8_slider.setProperty("value", 0)
        self.motor_8_slider.setOrientation(QtCore.Qt.Vertical)
        self.motor_8_slider.setObjectName("motor_8_slider")
        self.gridLayout_3.addWidget(self.motor_8_slider, 2, 0, 1, 1)
        self.motor_h_layout.addWidget(self.motor_8_brv)
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1436, 26))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.console.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'MS Shell Dlg 2\'; font-size:6.6pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;\">Console:</p></body></html>"))
        self.e_stop_button.setText(_translate("MainWindow", "E-STOP"))
        self.neutral_button.setText(_translate("MainWindow", "Neutral"))
        self.dive_button.setText(_translate("MainWindow", "Dive"))
        self.surface_button.setText(_translate("MainWindow", "Surface"))
        self.all_motors_button.setText(_translate("MainWindow", "All Motors"))
        self.seq_test_button.setText(_translate("MainWindow", "Sequential Test"))
        self.forward_button.setText(_translate("MainWindow", "Forward"))
        self.hover_forward_button.setText(_translate("MainWindow", "HoverForward"))
        self.reverse_button.setText(_translate("MainWindow", "Reverse"))
        self.hover_spin_button.setText(_translate("MainWindow", "HoverSpin"))
        self.label_16.setText(_translate("MainWindow", "Depth"))
        self.label_5.setText(_translate("MainWindow", "Altitude"))
        self.label_7.setText(_translate("MainWindow", "Temperature"))
        self.label_6.setText(_translate("MainWindow", "Pressure"))
        self.label.setText(_translate("MainWindow", "Pitch"))
        self.label_3.setText(_translate("MainWindow", "Yaw"))
        self.label_4.setText(_translate("MainWindow", "Roll"))
        self.label_8.setText(_translate("MainWindow", "Motor 1: LH"))
        self.label_9.setText(_translate("MainWindow", "Motor 2: RH"))
        self.label_15.setText(_translate("MainWindow", "Motor 3: FH"))
        self.label_13.setText(_translate("MainWindow", "Motor 4: BH"))
        self.label_14.setText(_translate("MainWindow", "Motor 5: FLV"))
        self.label_11.setText(_translate("MainWindow", "Motor 6: FRV"))
        self.label_12.setText(_translate("MainWindow", "Motor 7: BLV"))
        self.label_10.setText(_translate("MainWindow", "Motor 8: BRV"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
