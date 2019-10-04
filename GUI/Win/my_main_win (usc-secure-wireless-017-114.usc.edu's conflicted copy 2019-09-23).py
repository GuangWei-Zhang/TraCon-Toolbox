# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'main_win.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QFileDialog
import Batch_OFT
import cv2
from PyQt5.QtMultimedia import *
from PyQt5.QtMultimediaWidgets import *
import os
import sys
import Batch_EPM
import Batch_PlacePreference
import TraCon_looming
import AutoPlacePreference

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(817, 598)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton_CameraPreview = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_CameraPreview.setGeometry(QtCore.QRect(40, 10, 121, 32))
        self.pushButton_CameraPreview.setObjectName("pushButton_CameraPreview")
        self.pushButton_CameraPreview.clicked.connect(self.camera_preview)
        self.textEdit_filename = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_filename.setGeometry(QtCore.QRect(160, 50, 521, 31))
        self.textEdit_filename.setObjectName("textEdit_filename")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(50, 60, 101, 16))
        self.label.setObjectName("label")
        self.pushButton_browse = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_browse.setGeometry(QtCore.QRect(690, 50, 113, 32))
        self.pushButton_browse.setObjectName("pushButton_browse")
        self.pushButton_browse.clicked.connect(self.ask_save_mp4)
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(220, 150, 101, 16))
        self.label_3.setObjectName("label_3")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(220, 110, 111, 101))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_2.setObjectName("label_2")
        self.label_4 = QtWidgets.QLabel(self.centralwidget)
        self.label_4.setGeometry(QtCore.QRect(360, 100, 111, 111))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("lpm.png"))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.centralwidget)
        self.label_5.setGeometry(QtCore.QRect(350, 150, 121, 16))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.centralwidget)
        self.label_6.setGeometry(QtCore.QRect(500, 110, 111, 101))
        self.label_6.setText("")
        self.label_6.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_6.setObjectName("label_6")
        self.label_7 = QtWidgets.QLabel(self.centralwidget)
        self.label_7.setGeometry(QtCore.QRect(500, 150, 121, 16))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.centralwidget)
        self.label_8.setGeometry(QtCore.QRect(240, 300, 121, 16))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.centralwidget)
        self.label_9.setGeometry(QtCore.QRect(220, 260, 111, 101))
        self.label_9.setText("")
        self.label_9.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_9.setObjectName("label_9")
        self.label_10 = QtWidgets.QLabel(self.centralwidget)
        self.label_10.setGeometry(QtCore.QRect(360, 260, 111, 101))
        self.label_10.setText("")
        self.label_10.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_10.setObjectName("label_10")
        self.label_11 = QtWidgets.QLabel(self.centralwidget)
        self.label_11.setGeometry(QtCore.QRect(380, 300, 121, 16))
        self.label_11.setObjectName("label_11")
        self.label_12 = QtWidgets.QLabel(self.centralwidget)
        self.label_12.setGeometry(QtCore.QRect(500, 260, 111, 101))
        self.label_12.setText("")
        self.label_12.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_12.setObjectName("label_12")
        self.label_13 = QtWidgets.QLabel(self.centralwidget)
        self.label_13.setGeometry(QtCore.QRect(530, 300, 121, 16))
        self.label_13.setObjectName("label_13")
        self.label_14 = QtWidgets.QLabel(self.centralwidget)
        self.label_14.setGeometry(QtCore.QRect(50, 150, 60, 16))
        self.label_14.setObjectName("label_14")
        self.label_15 = QtWidgets.QLabel(self.centralwidget)
        self.label_15.setGeometry(QtCore.QRect(50, 300, 141, 16))
        self.label_15.setObjectName("label_15")
        self.label_16 = QtWidgets.QLabel(self.centralwidget)
        self.label_16.setGeometry(QtCore.QRect(630, 260, 111, 101))
        self.label_16.setText("")
        self.label_16.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_16.setObjectName("label_16")
        self.label_17 = QtWidgets.QLabel(self.centralwidget)
        self.label_17.setGeometry(QtCore.QRect(650, 300, 121, 16))
        self.label_17.setObjectName("label_17")
        self.label_18 = QtWidgets.QLabel(self.centralwidget)
        self.label_18.setGeometry(QtCore.QRect(10, 460, 201, 16))
        self.label_18.setObjectName("label_18")
        self.label_19 = QtWidgets.QLabel(self.centralwidget)
        self.label_19.setGeometry(QtCore.QRect(220, 410, 111, 101))
        self.label_19.setText("")
        self.label_19.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_19.setObjectName("label_19")
        self.label_20 = QtWidgets.QLabel(self.centralwidget)
        self.label_20.setGeometry(QtCore.QRect(240, 460, 61, 16))
        self.label_20.setObjectName("label_20")
        self.pushButton_OFT = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_OFT.setGeometry(QtCore.QRect(212, 210, 121, 32))
        self.pushButton_OFT.setObjectName("pushButton_OFT")
        self.pushButton_OFT.clicked.connect(self.open_field_test_click)
        self.pushButton_EPM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_EPM.setGeometry(QtCore.QRect(340, 210, 141, 32))
        self.pushButton_EPM.setObjectName("pushButton_EPM")
        self.pushButton_EPM.clicked.connect(self.elevated_plus_maze_click)
        self.pushButton_MWM = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_MWM.setGeometry(QtCore.QRect(480, 210, 141, 32))
        self.pushButton_MWM.setObjectName("pushButton_MWM")
        self.pushButton_Auto2chamber = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Auto2chamber.setGeometry(QtCore.QRect(210, 360, 131, 32))
        self.pushButton_Auto2chamber.setObjectName("pushButton_Auto2chamber")
        self.pushButton_Auto2chamber.clicked.connect(self.auto_RPP_click)
        self.pushButton_3chamber = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3chamber.setGeometry(QtCore.QRect(350, 360, 121, 32))
        self.pushButton_3chamber.setObjectName("pushButton_3chamber")
        self.pushButton_Conner = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Conner.setGeometry(QtCore.QRect(490, 360, 121, 32))
        self.pushButton_Conner.setObjectName("pushButton_Conner")
        self.pushButton_Looming = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Looming.setGeometry(QtCore.QRect(620, 360, 121, 32))
        self.pushButton_Looming.setObjectName("pushButton_Looming")
        self.pushButton_Looming.clicked.connect(self.looming_click)
        self.pushButton_Social = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_Social.setGeometry(QtCore.QRect(210, 510, 121, 32))
        self.pushButton_Social.setObjectName("pushButton_Social")
        self.pushButton_2chamber = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2chamber.setGeometry(QtCore.QRect(620, 210, 181, 32))
        self.pushButton_2chamber.setObjectName("pushButton_2chamber")
        self.pushButton_2chamber.clicked.connect(self.realtime_Place_Preference_click)
        self.label_21 = QtWidgets.QLabel(self.centralwidget)
        self.label_21.setGeometry(QtCore.QRect(630, 110, 111, 101))
        self.label_21.setPixmap(QtGui.QPixmap("oft1.png"))
        self.label_21.setObjectName("label_21")
        self.label_22 = QtWidgets.QLabel(self.centralwidget)
        self.label_22.setGeometry(QtCore.QRect(630, 170, 121, 16))
        self.label_22.setObjectName("label_22")
        self.columnView = QtWidgets.QColumnView(self.centralwidget)
        self.columnView.setGeometry(QtCore.QRect(10, 100, 791, 141))
        self.columnView.setObjectName("columnView")
        self.columnView_2 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_2.setGeometry(QtCore.QRect(10, 250, 791, 141))
        self.columnView_2.setObjectName("columnView_2")
        self.columnView_3 = QtWidgets.QColumnView(self.centralwidget)
        self.columnView_3.setGeometry(QtCore.QRect(10, 400, 791, 141))
        self.columnView_3.setObjectName("columnView_3")
        self.textEdit_ArduinoDeviceName = QtWidgets.QTextEdit(self.centralwidget)
        self.textEdit_ArduinoDeviceName.setGeometry(QtCore.QRect(320, 10, 471, 31))
        self.textEdit_ArduinoDeviceName.setObjectName("textEdit_ArduinoDeviceName")
        self.label_23 = QtWidgets.QLabel(self.centralwidget)
        self.label_23.setGeometry(QtCore.QRect(180, 10, 141, 20))
        self.label_23.setObjectName("label_23")
        self.columnView_3.raise_()
        self.columnView_2.raise_()
        self.columnView.raise_()
        self.label_9.raise_()
        self.label_2.raise_()
        self.pushButton_CameraPreview.raise_()
        self.textEdit_filename.raise_()
        self.label.raise_()
        self.pushButton_browse.raise_()
        self.label_3.raise_()
        self.label_4.raise_()
        self.label_5.raise_()
        self.label_6.raise_()
        self.label_7.raise_()
        self.label_8.raise_()
        self.label_10.raise_()
        self.label_11.raise_()
        self.label_12.raise_()
        self.label_13.raise_()
        self.label_14.raise_()
        self.label_15.raise_()
        self.label_16.raise_()
        self.label_17.raise_()
        self.label_18.raise_()
        self.label_19.raise_()
        self.label_20.raise_()
        self.pushButton_OFT.raise_()
        self.pushButton_EPM.raise_()
        self.pushButton_MWM.raise_()
        self.pushButton_Auto2chamber.raise_()
        self.pushButton_3chamber.raise_()
        self.pushButton_Conner.raise_()
        self.pushButton_Looming.raise_()
        self.pushButton_Social.raise_()
        self.pushButton_2chamber.raise_()
        self.label_21.raise_()
        self.label_22.raise_()
        self.textEdit_ArduinoDeviceName.raise_()
        self.label_23.raise_()
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 817, 22))
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
        self.pushButton_CameraPreview.setText(_translate("MainWindow", "Camera Preview"))
        self.label.setText(_translate("MainWindow", "Outout Filename"))
        self.pushButton_browse.setText(_translate("MainWindow", "Browse"))
        self.label_3.setText(_translate("MainWindow", "Open Field Test"))
        self.label_5.setText(_translate("MainWindow", "Elevated Plus Maze"))
        self.label_7.setText(_translate("MainWindow", "Morris Water Maze"))
        self.label_8.setText(_translate("MainWindow", "2-Chamber"))
        self.label_11.setText(_translate("MainWindow", "3-Chamber"))
        self.label_13.setText(_translate("MainWindow", "Conner"))
        self.label_14.setText(_translate("MainWindow", "Detection"))
        self.label_15.setText(_translate("MainWindow", "Close-loop Stimulation"))
        self.label_17.setText(_translate("MainWindow", "Looming"))
        self.label_18.setText(_translate("MainWindow", "Dynamic Detection & Stimulation"))
        self.label_20.setText(_translate("MainWindow", "Social"))
        self.pushButton_OFT.setText(_translate("MainWindow", "Open Field Test"))
        self.pushButton_EPM.setText(_translate("MainWindow", "Elevated Plus Maze"))
        self.pushButton_MWM.setText(_translate("MainWindow", "Morris Water Maze"))
        self.pushButton_Auto2chamber.setText(_translate("MainWindow", "Auto 2-Chamber"))
        self.pushButton_3chamber.setText(_translate("MainWindow", "3-Chamber"))
        self.pushButton_Conner.setText(_translate("MainWindow", "Conner"))
        self.pushButton_Looming.setText(_translate("MainWindow", "Looming"))
        self.pushButton_Social.setText(_translate("MainWindow", "Social"))
        self.pushButton_2chamber.setText(_translate("MainWindow", "Realtime Place Preference"))
        self.label_21.setText(_translate("MainWindow", "Realtime Place Preference"))
        self.label_22.setText(_translate("MainWindow", "Realtime Place Preference"))
        self.textEdit_ArduinoDeviceName.setHtml(_translate("MainWindow", "<!DOCTYPE HTML PUBLIC \"-//W3C//DTD HTML 4.0//EN\" \"http://www.w3.org/TR/REC-html40/strict.dtd\">\n"
"<html><head><meta name=\"qrichtext\" content=\"1\" /><style type=\"text/css\">\n"
"p, li { white-space: pre-wrap; }\n"
"</style></head><body style=\" font-family:\'.SF NS Text\'; font-size:13pt; font-weight:400; font-style:normal;\">\n"
"<p style=\" margin-top:12px; margin-bottom:12px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px; background-color:#ffffff;\"><span style=\" font-family:\'Menlo\'; color:#000000;\">/dev/cu.usbmodem14101</span></p></body></html>"))
        self.label_23.setText(_translate("MainWindow", "Arduino Device Name"))

    def ask_save_mp4(self):
        self.dlg=QFileDialog()
        self.output_filename = self.dlg.getSaveFileName(self.dlg, 'Save file',os.getenv('HOME'), "Video files (*.mp4 *.mov)")
        self.textEdit_filename.setPlainText(self.output_filename[0])

    def open_field_test_click(self):
        Batch_OFT.run_OFT(self)

    def stop_click(self):
        Batch_OFT.stop_OFT(self)

    def elevated_plus_maze_click(self):
        Batch_EPM.run_EPM(self)

    def realtime_Place_Preference_click(self):
        Batch_PlacePreference.run_RPP(self)

    def looming_click(self):
        self.get_ArduinoDeviceName()
        self.get_output_filename()
        TraCon_looming.run_looming(self)

    def auto_RPP_click(self):
        self.get_ArduinoDeviceName()
        self.get_output_filename()
        AutoPlacePreference.run_autoRPP(self)

    def get_ArduinoDeviceName(self):
        self.arduino_device = self.textEdit_ArduinoDeviceName.toPlainText()

    def get_output_filename(self):
        self.output_filename=self.textEdit_filename.toPlainText()

    def camera_preview(self):
        self.online_webcams = QCameraInfo.availableCameras()
        if not self.online_webcams:
            pass  # quit
        self.exist = QCameraViewfinder()
        self.exist.show()
        camera_window=cameraWindow()
        camera_window.setCentralWidget(self.exist)
        # set the default webcam.
        self.get_webcam(0)
        camera_window.setWindowTitle("Camera Preview")
        camera_window.show()

    def get_webcam(self, i):
        self.my_webcam = QCamera(self.online_webcams[i])
        self.my_webcam.setViewfinder(self.exist)
        self.my_webcam.setCaptureMode(QCamera.CaptureStillImage)
        self.my_webcam.error.connect(lambda: self.alert(self.my_webcam.errorString()))
        self.my_webcam.start()
        print('start')

    def alert(self, s):
        """
        This handle errors and displaying alerts.
        """
        err = QErrorMessage(self)
        err.showMessage(s)

class cameraWindow(QtWidgets.QMainWindow):
    def closeEvent(self):
        print('closeing')
        self.my_webcam = QCamera(self.online_webcams[0])
        self.my_webcam.stop()
        event.accept()
